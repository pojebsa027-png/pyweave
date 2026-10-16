from flask import redirect, render_template, url_for

from app import app, db
from forms import TaskForm
from models import Task


@app.route("/")
@app.route("/index")
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = TaskForm()
    if form.validate_on_submit():
        db.session.add(Task(title=form.title.data))
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html", form=form)
