"""Step 06 — wire up SQLAlchemy and define the Task model."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-only-change-me"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

import routes  # noqa: E402,F401  (routes import `db` back out of here)


@app.shell_context_processor
def shell_context():
    from models import Task

    return {"db": db, "Task": Task}


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
