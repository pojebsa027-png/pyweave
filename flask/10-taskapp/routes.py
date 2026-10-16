from flask import abort, flash, redirect, render_template, url_for

from app import app, db
from forms import DeleteForm, TaskForm
from models import Task


def get_task_or_404(task_id: int) -> Task:
    task = db.session.get(Task, task_id)
    if task is None:
        abort(404)
    return task


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
        flash("Task added.", "success")
        return redirect(url_for("index"))
    return render_template("add.html", form=form)


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id: int):
    task = get_task_or_404(task_id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        db.session.commit()
        flash("Task updated.", "success")
        return redirect(url_for("index"))
    return render_template("edit.html", form=form, task=task)


@app.route("/delete/<int:task_id>", methods=["GET", "POST"])
def delete(task_id: int):
    task = get_task_or_404(task_id)
    form = DeleteForm()
    if form.validate_on_submit():
        db.session.delete(task)
        db.session.commit()
        flash("Task deleted.", "warning")
        return redirect(url_for("index"))
    return render_template("delete.html", form=form, task=task)
