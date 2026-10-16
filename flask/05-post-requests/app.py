"""Step 05 — the same form, now actually handled on POST."""
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-only-change-me"

import routes  # noqa: E402,F401

if __name__ == "__main__":
    app.run(debug=True)
