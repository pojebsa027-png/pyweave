from flask import render_template

from app import app
from forms import TaskForm


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    form = TaskForm()
    title = None
    if form.validate_on_submit():
        title = form.title.data
    return render_template("about.html", form=form, title=title)
