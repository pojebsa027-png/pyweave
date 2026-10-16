"""Step 02 — render a template instead of returning a bare string."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", current_title="Notes")


if __name__ == "__main__":
    app.run(debug=True)
