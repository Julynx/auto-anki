# -*- coding: utf-8 -*-
"""
Main module for generating Anki flashcards in CSV format using OpenAI's o4-mini model.

Reads topics from topics.py, builds prompts with config.py, calls the OpenAI API,
and saves the results in the 'out' folder.
"""

import logging
import re
from pathlib import Path
from typing import List

from dotenv import load_dotenv
import openai

from topics import topics
from config import build_prompt

OUT_DIR = Path("out")
MODEL_NAME = "o4-mini"

# Load environment variables before creating the OpenAI client
load_dotenv()
OPENAI_CLIENT = openai.OpenAI()


def ensure_output_dir(directory: Path) -> None:
    """
    Create the output directory if it does not exist.
    """
    try:
        directory.mkdir(exist_ok=True)
    except OSError as exc:
        logging.error("Failed to create output directory '%s': %s", directory, exc)
        raise


def run_o4_mini(prompt_text: str) -> str:
    """
    Call OpenAI's o4-mini model with the given prompt and return the response.
    Compatible with openai>=1.0.0.
    """
    try:
        response = OPENAI_CLIENT.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt_text}]
        )
        return response.choices[0].message.content.strip()
    except Exception as exc:
        logging.error("Error calling OpenAI: %s", exc)
        raise


def fix_semicolons_in_csv_content(content: str) -> str:
    """
    For each line, replace any semicolons after the first one with commas.
    """

    def fix_line(line):
        first, *rest = line.rstrip("\n").split(";")
        if not rest:
            return line
        return first + ";" + ",".join(rest)

    return "\n".join(fix_line(line) for line in content.splitlines() if line.strip())


def save_csv(output_path: Path, content: str) -> None:
    """
    Save the content to a CSV file at the specified path,
    ensuring that only the first semicolon in each line is kept.
    """
    try:
        fixed_content = fix_semicolons_in_csv_content(content)
        with output_path.open("w", encoding="utf-8") as file:
            if not fixed_content.endswith("\n"):
                file.write(fixed_content + "\n")
            else:
                file.write(fixed_content)
    except OSError as exc:
        logging.error("Failed to save file '%s': %s", output_path, exc)
        raise


def sanitize_filename(name: str) -> str:
    """
    Sanitize a string to be safe for use as a filename.
    Replaces spaces and non-alphanumeric characters with underscores.
    """
    # Remove leading/trailing whitespace, replace spaces and non-alphanu
    # with underscores, collapse multiple underscores
    sanitized = re.sub(r"[^A-Za-z0-9]+", "_", name.strip())
    return sanitized.strip("_")


def process_topics(topic_list: List[str], output_dir: Path) -> None:
    """
    Process a list of topics: generate prompts, call the model, and save the results.
    """
    for topic in topic_list:
        filename = sanitize_filename(topic) + ".csv"
        output_path = output_dir / filename
        prompt_text = build_prompt(topic)
        logging.info("Generating %s ...", output_path.name)
        try:
            output = run_o4_mini(prompt_text)
            save_csv(output_path, output)
        except (OSError, openai.OpenAIError) as exc:
            logging.error(
                "Error generating '%s': %s",
                output_path.name,
                exc
            )


def main() -> None:
    """
    Main entry point of the script.
    """
    # Load environment variables from .env
    load_dotenv()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    ensure_output_dir(OUT_DIR)
    process_topics(topics, OUT_DIR)


if __name__ == "__main__":
    main()
