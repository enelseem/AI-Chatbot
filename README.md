# 🤖 AI Chatbot

A simple AI-powered chatbot built with **Streamlit** and the **Claude API** (Anthropic).

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-red)
![Claude](https://img.shields.io/badge/Powered%20by-Claude-orange)

## ✨ Features

- 💬 Real-time chat with AI (Claude)
- 🧠 Customizable AI personality via System Prompt
- 🗑️ Clear chat button
- 🌙 Dark mode UI
- 📱 Responsive layout

## 🚀 Getting Started

### 1. Clone this repo
```bash
git clone https://github.com/enelseem/AI-Chatbot.git
cd AI-Chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API Key

Create a `.env` file from the example:
```bash
cp .env.example .env
```

Fill in your `ANTHROPIC_API_KEY` from [console.anthropic.com](https://console.anthropic.com).

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🌐 Deploy to Streamlit Cloud (Free!)

1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Under **Secrets**, add:
```toml
ANTHROPIC_API_KEY = "sk-ant-..."
```
5. Deploy! 🎉

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | UI / Frontend |
| [Anthropic Python SDK](https://github.com/anthropic-ai/anthropic-sdk-python) | Claude API |
| Python 3.9+ | Backend |

---

## 📄 License

MIT License — free to use and modify.
