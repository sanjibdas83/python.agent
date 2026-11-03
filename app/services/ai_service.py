from __future__ import annotations

from openai import OpenAI

from app.config import settings


class AIService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else None

    def generate_response(self, user_message: str, db_context: str = "") -> str:
        if not self.client:
            return (
                "OpenAI API key is not configured. The assistant is running in local fallback mode. "
                f"User request: {user_message}. "
                f"Oracle context: {db_context or 'No Oracle context provided'}"
            )

        system_prompt = (
            "You are a helpful AI assistant for a Python application connected to an Oracle database. "
            "Answer concisely and use the provided database context when relevant."
        )

        response = self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Database context: {db_context}\n\nUser request: {user_message}"},
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content.strip()
