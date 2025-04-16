# 🤖 Telegram Content Bot
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://t.me/OFFpolice2069) [![aiogram](https://img.shields.io/badge/aiogram-3.4.1-%234FC3F7)](https://docs.aiogram.dev/en/latest/) [![aiohttp](https://img.shields.io/badge/aiohttp-latest-%23005788)](https://docs.aiohttp.org/en/stable/) [![google-generativeai](https://img.shields.io/badge/google--generativeai-latest-%23FF6D01)](https://pypi.org/project/google-generativeai/)

A Telegram bot that generates themed posts (text + image) using the [Gemini API (Google Generative AI)](https://ai.google.dev/) and sends them to a chat via the `/post` command.  

---

## 🚀 Features

- Generates posts on random topics
- Text + valid cover image (or `fallback.jpg` if none)
- `/post` command for manual triggering
- Dockerized and easily deployable via `docker-compose`

---

## 🧠 Technologies Used

- [aiogram 3.x](https://docs.aiogram.dev/en/latest/) — asynchronous Telegram bot framework
- [Google Generative AI SDK](https://pypi.org/project/google-generativeai/) — access to Gemini
- [aiohttp](https://docs.aiohttp.org/en/stable/) — async HTTP requests
- [Docker](https://www.docker.com/) + [Docker Compose](https://docs.docker.com/compose/) — for containerization

---

## 📦 Installation & Launch

### 1. Clone the repository

```bash
git clone https://github.com/serejekee/echogem.git
cd telegram-content-bot
```

### 2. Add a `.env` file with tokens
```env
BOT_TOKEN=your_telegram_bot_token
GOOGLE_API_KEY=your_google_api_key
```
- How to get BOT_TOKEN?
[FOLLOW](https://t.me/BotFather)
- How to get GOOGLE_API_KEY?
[FOLLOW](https://aistudio.google.com/app/apikey)
### 3. Build and run the container
```bash
docker-compose up --build -d
```

Done! The bot will start listening for commands.

---

## 💬 Usage

`/post` — generate a post on a random topic (e.g., Space, AI, Health, etc.)

Optional: you can easily extend it to accept a custom topic with `/post topic`.

---

## 📁 Project Structure

```structure
my_bot/
├── bot/                    # Contains the bot's main logic and handlers
│   ├── __init__.py
│   ├── main.py             # Telegram bot logic
│   ├── handlers.py         # Bot command handlers
│   ├── utils.py            # Utility functions (like generating posts, etc.)
├── data/                   # Contains all necessary data files
│   ├── prompt.txt          # Add your prompt here
│   ├── topics.txt          # Add your topics here
│   ├── fallback.jpg        # Fallback image if there is no picture
├── Dockerfile              # Docker build instructions
├── docker-compose.yml      # Docker container setup
├── requirements.txt        # Dependencies
├── README.md               # Documentation

```

---

## 📜 License

[MIT License](MIT) — free to use, adapt, and improve 🤘

---

## 🤝 Contact
[![Telegram Badge](https://img.shields.io/badge/Contact-blue?style=flat&logo=telegram&logoColor=white)](https://t.me/spystars777)

