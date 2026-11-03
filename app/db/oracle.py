from __future__ import annotations

try:
    import oracledb
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    oracledb = None

from app.config import settings


def get_connection():
    if oracledb is None:
        raise ModuleNotFoundError(
            "oracledb is not installed. Install it separately when Oracle connectivity is needed."
        )

    if not settings.oracle_password:
        raise ValueError("ORACLE_PASSWORD is not configured.")

    return oracledb.connect(
        user=settings.oracle_user,
        password=settings.oracle_password,
        dsn=settings.oracle_dsn,
    )


def execute_query(query: str, params: tuple | list | None = None):
    if oracledb is None:
        raise ModuleNotFoundError(
            "oracledb is not installed. Install it separately when Oracle connectivity is needed."
        )

    with get_connection() as connection:
        with connection.cursor() as cursor:
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)
            return cursor.fetchall()


def test_connection() -> bool:
    if oracledb is None:
        return False

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 FROM dual")
                row = cursor.fetchone()
                return bool(row and row[0] == 1)
    except Exception:
        return False
