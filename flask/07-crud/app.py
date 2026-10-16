"""Step 07 — list and create rows against the database."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-only-change-me"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

import routes  # noqa: E402,F401


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
