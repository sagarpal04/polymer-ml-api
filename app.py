from api.predict import app


if __name__ == "__main__":
    # Simple message when run directly; uvicorn should be used to serve the app.
    print("This module exposes `app` for ASGI servers (uvicorn). Run: uvicorn app:app --reload")
