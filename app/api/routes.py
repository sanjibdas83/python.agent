from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse
from app.services.ai_service import AIService
from app.services.oracle_query_service import OracleQueryService

router = APIRouter()
ai_service = AIService()
oracle_service = OracleQueryService()


@router.get("/health")
def healthcheck():
    return {"status": "ok", "service": "oracle-ai-chatbot"}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    db_connected = False
    db_context = "Oracle database is not reachable."

    try:
        db_connected = oracle_service.validate_connection()
        if db_connected:
            db_context = "Oracle database connection established successfully."
    except Exception as exc:  # pragma: no cover - defensive logging path
        db_context = f"Oracle connection failed: {exc}"

    reply = ai_service.generate_response(request.message, db_context)

    return ChatResponse(
        response=reply,
        session_id=request.session_id or "local-session",
        db_connected=db_connected,
    )
