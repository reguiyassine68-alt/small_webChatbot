# YaGui-Bot

A lightweight web chat application powered by **Flask**, the **OpenAI Python SDK** configured for the **Groq API**, and a clean **HTML/CSS/JavaScript** chat interface with conversation history and chat reset support.

## Tech Stack
- **Backend:** Python, Flask, OpenAI SDK (`base_url="https://api.groq.com/openai/v1"`), `python-dotenv`
- **Model:** `openai/gpt-oss-20b` via Groq API
- **Frontend:** HTML, CSS, Vanilla JavaScript (`fetch` API)

## Links
-Groq API Key:  https://console.groq.com/keys

## Project Structure
```text
app1_bot/
├── .env              # Local secrets (not committed to Git)
├── .env.example      # Example environment variables
├── .gitignore        # Ignored files and folders
├── backend.py        # Flask server and chat/reset endpoints
└── templates/        # Or `frontend/` if configured via `template_folder`
    └── home.html     # Chat UI

