from __future__ import annotations

from app.db.oracle import test_connection, execute_query


class OracleQueryService:
    def validate_connection(self) -> bool:
        return test_connection()

    def fetch_system_date(self):
        return execute_query("SELECT SYSDATE AS current_date FROM dual")

    def fetch_user_count(self):
        return execute_query("SELECT COUNT(*) AS total_rows FROM user_tables")
