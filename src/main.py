from waitress import serve

from src.server import app

if __name__ == "__main__":
    serve(app, listen="*:8080")
