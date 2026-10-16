# flask/

Ten standalone apps. Each directory is runnable on its own and adds exactly one
concept to the one before it — read them in order.

| Step | Concept | Files |
|---|---|---|
| `01-minimal-app` | a route that returns a string | `app.py` |
| `02-html-templates` | `render_template`, context values | `app.py`, `templates/` |
| `03-layouts` | template inheritance, a second page | `app.py`, `templates/` |
| `04-forms` | Flask-WTF, CSRF, validators | `app.py`, `forms.py`, `routes.py` |
| `05-post-requests` | handling a submitted form | same |
| `06-database` | Flask-SQLAlchemy, the `Task` model | `+ models.py` |
| `07-crud` | list + create against the database | same |
| `08-bootstrap` | a real page shell | `templates/` |
| `09-edit` | update an existing row | `+ templates/edit.html` |
| `10-taskapp` | delete, flash messages, pinned deps | the finished app |

## Running any step

```bash
cd 10-taskapp
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Steps 01–05 need only `Flask` and `Flask-WTF`. Steps 06+ also need
`Flask-SQLAlchemy`. `10-taskapp/requirements.txt` has the full set.

## Why the early steps keep templates inline

Because the diff between two steps should be the only thing you have to read.
Once the app grows a layout (`03-layouts`), templates move into `templates/` and
stay there.
