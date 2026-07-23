# Sentinel AI Security

> An AI security gateway for LLM applications that inspects prompts and model outputs, enforces policy rules, and surfaces analytics to help teams catch prompt injection, data leakage, and unsafe responses before they reach users.

> **Status:** 🚧 Work in Progress

---

## Features

### Current
- FastAPI backend
- Application factory setup
- Health/root endpoint
- Modular project structure

### Planned
- Prompt firewall (injection & jailbreak detection)
- Output firewall (PII/secret leakage detection)
- Policy engine with configurable rules
- Request/response logging & audit trail
- Rate limiting and abuse detection
- Analytics dashboard (blocked vs allowed requests)
- Model/provider-agnostic proxy (OpenAI, Anthropic, Ollama, etc.)
- Custom rule authoring (regex, keyword, ML-based)
- Real-time alerting (Slack/email/webhook)
- Role-based access control
- API key management for downstream apps
- Report generation (PDF/JSON)

---

## Tech Stack

### Backend
- Python
- FastAPI
- Pydantic
- Uvicorn

### Database
- TBD

### AI
- Provider-agnostic (OpenAI, Anthropic, Ollama, etc.)

### Security
- Prompt/output inspection
- Policy engine
- Rate limiting

---

## Project Structure

```text
Sentinel AI Security/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── __init__.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-org>/sentinel-ai-security.git
cd sentinel-ai-security
```

---

### 2. Create a virtual environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

### 4. Run the application

```bash
uvicorn app.main:app --reload
```

The API will start on