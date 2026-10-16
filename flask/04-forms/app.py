"""Step 04 — split the app object from the routes, add a CSRF-protected form."""
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-only-change-me"

import routes  # noqa: E402,F401  (routes need `app`, so this import comes last)

if __name__ == "__main__":
    app.run(debug=True)
