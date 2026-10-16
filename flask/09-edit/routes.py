from flask import abort, redirect, render_template, url_for

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


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id: int):
    task = db.session.get(Task, task_id) or abort(404)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", form=form, task=task)
