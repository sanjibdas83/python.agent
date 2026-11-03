# Oracle AI Chat Assistant

This project scaffolds a Python FastAPI chatbot that can connect to an Oracle database and use an AI model for natural-language responses.

## Features
- FastAPI backend
- Oracle DB connectivity via `oracledb`
- AI response generation via OpenAI-compatible API
- Health and chat endpoints
- Environment-based configuration

## Project structure
```text
app/
  api/
  db/
  models/
  services/
  config.py
  main.py
scripts/
tests/
requirements.txt
.env.example
```

## Setup
1. Create a virtual environment.
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and update values.
4. Run the app:
   ```bash
   python main.py
   ```

## API example
```bash
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Show me the current Oracle system date."}'
```

## Notes
- Oracle client libraries may need to be installed separately depending on your environment.
- The project is intentionally set up as a starter backend for a database-connected AI assistant.
