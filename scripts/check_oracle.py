from app.db.oracle import test_connection


if __name__ == "__main__":
    try:
        status = test_connection()
        print(f"Oracle connection status: {status}")
    except Exception as exc:  # pragma: no cover
        print(f"Oracle connection error: {exc}")
