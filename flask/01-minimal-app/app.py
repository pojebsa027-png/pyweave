"""Step 01 — the smallest possible Flask application."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Hello from PyWeave."


if __name__ == "__main__":
    app.run(debug=True)
