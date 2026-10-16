from flask import render_template

from app import app
from models import Task


@app.route("/")
@app.route("/index")
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)
