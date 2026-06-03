# 🤖 AI Chatbot

Chatbot sederhana berbasis AI yang dibangun dengan **Streamlit** dan **Claude API** (Anthropic).

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-red)
![Claude](https://img.shields.io/badge/Powered%20by-Claude-orange)

## ✨ Fitur

- 💬 Chat real-time dengan AI (Claude)
- 🧠 Bisa kustomisasi kepribadian AI lewat System Prompt
- 🗑️ Tombol clear chat
- 🌙 Dark mode UI
- 📱 Responsive layout

## 🚀 Cara Jalankan

### 1. Clone repo ini
```bash
git clone https://github.com/username/ai-chatbot.git
cd ai-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup API Key

Buat file `.env` dari contoh:
```bash
cp .env.example .env
```

Isi `ANTHROPIC_API_KEY` dengan API key kamu dari [console.anthropic.com](https://console.anthropic.com).

### 4. Jalankan app
```bash
streamlit run app.py
```

Buka browser ke `http://localhost:8501`

---

## 🌐 Deploy ke Streamlit Cloud (Gratis!)

1. Push repo ini ke GitHub
2. Buka [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect GitHub repo kamu
4. Di **Secrets**, tambahkan:
```toml
ANTHROPIC_API_KEY = "sk-ant-..."
```
5. Deploy! 🎉

---

## 🛠️ Tech Stack

| Tool | Kegunaan |
|------|----------|
| [Streamlit](https://streamlit.io) | UI / Frontend |
| [Anthropic Python SDK](https://github.com/anthropic-ai/anthropic-sdk-python) | Claude API |
| Python 3.9+ | Backend |

---

## 📄 License

MIT License — bebas dipakai dan dimodifikasi.
