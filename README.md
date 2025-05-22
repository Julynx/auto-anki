# 🧠 Anki Card Generator with o4-mini 🚀

Generate expert-level Anki flashcards in CSV format from curated topic lists, powered by OpenAI's `o4-mini` model. Perfect for advanced technical exam prep, elite competitions, or deep-dive learning!

---

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-o4--mini-10a37f?logo=openai)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Ready_to_Use-Yes-brightgreen)

---

## ✨ Features

- **Automated Generation**: Instantly create CSV files with double-sided Anki cards for each topic.
- **Expert-Level Content**: Prompts are designed for advanced, real-world technical mastery.
- **Customizable**: Easily adjust language and number of questions per topic.
- **Robust & Reliable**: Handles API/network errors and logs progress.
- **Ready for Anki**: Output is perfectly formatted for direct import.

---

<details>
<summary>📂 <strong>Project Structure</strong> (click to expand)</summary>

```
.
├── config.py           # Prompt builder & settings (language, # questions)
├── generate.py         # Main script: generates CSVs using OpenAI
├── topics.py           # Topic lists (common, d2, d3)
├── .env                # Your OpenAI API key (not included)
└── out/                # Output CSV files (auto-created)
```
</details>

---

## ⚡️ Quickstart

### 1. **Requirements**

- Python 3.8+
- OpenAI API key with access to `o4-mini`
- [uv](https://github.com/astral-sh/uv) (recommended for environment management)

### 2. **Setup**

```bash
# Clone this repo or download the files
git clone https://github.com/your-username/auto_anki.git
cd auto_anki

# Automatically install dependencies with uv
uv sync
```

### 3. **Configuration**

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_key_here
```

---

## 🛠️ Usage

Run the main script to generate your Anki cards:

```bash
uv run generate.py
```

- Output CSVs will appear in the `out/` folder, one per topic.

---

## 🧩 Customization

- **Change language, prompt or number of questions:**
  Edit `LANGUAGE`, `PROMPT` and `NUM_QUESTIONS` in `config.py`.
- **Add or modify topics:**
  Edit `topics.py` to update the topic lists.

---

## 💡 How It Works

1. **Topics** are loaded from `topics.py`.
2. **Prompts** are built using `config.py` (customizable!).
3. **OpenAI's o4-mini** generates Q&A pairs.
4. **CSV files** are saved in `out/`, ready for Anki import.

---

## 🙌 Contributing

Pull requests and suggestions are welcome!
Feel free to open an issue or fork the project.

---

## 📝 License

MIT License
