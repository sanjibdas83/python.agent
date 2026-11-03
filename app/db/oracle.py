from __future__ import annotations

from typing import Any

import oracledb

from app.config import settings


def get_connection():
    if not settings.oracle_password:
        raise ValueError("ORACLE_PASSWORD is not configured.")

    return oracledb.connect(
        user=settings.oracle_user,
        password=settings.oracle_password,
        dsn=settings.oracle_dsn,
    )


def execute_query(query: str, params: tuple | list | None = None):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)
            return cursor.fetchall()


def test_connection() -> bool:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM dual")
            row = cursor.fetchone()
            return bool(row and row[0] == 1)
