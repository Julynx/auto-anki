"""
Configuration module for generating Anki flashcards with o4-mini.
"""

LANGUAGE = "English (en-US)"

NUM_QUESTIONS = 20

PROMPT = """What follows is the name of a topic in {language} for an expert-level exam.

<topic>

Your task is to generate exactly {num_questions} double-sided Anki flashcards (in CSV format) containing expert-level questions and answers related to the topic. These cards are intended for a user preparing for elite-level technical certifications, advanced competitions, or high-difficulty technical interviews.

Guidelines:

- Each flashcard should have a clear, specific question (front) and a concise, technically accurate answer (back).

- Go beyond university level; questions should require deep understanding and expert-level insight.

- Cover a range of card types: key definitions, algorithm/formula analysis, tool/library usage, real-world scenarios, and trade-off/design decisions.

- Include content involving real-world tools, libraries, frameworks, and problem-solving techniques used by top professionals in the sector.

- Ensure all {num_questions} questions are unique (no duplicates or minor variations) and all answers are precise and accurate.

Output requirements:

- Output language: {language}

- CSV format: **exactly as shown**:
card_front_text;card_back_text
card_front_text;card_back_text
...

- **Do not include** explanations, headings or greetings in your response."""


def build_prompt(topic: str, language: str = LANGUAGE, num_questions: int = NUM_QUESTIONS) -> str:
    """
    Build the prompt for a given topic, allowing customization of language and number of questions.
    """
    return PROMPT.format(language=language, num_questions=num_questions).replace("<topic>", topic)
