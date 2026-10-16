# Task app — the finished Flask example

Add, edit and delete tasks against SQLite, with flash messages and a Bootstrap 5
shell.

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python app.py
```

→ http://127.0.0.1:5000/

The SQLite file lands in `instance/tasks.db`, created on first boot.

## Routes

| Path | Endpoint | Methods |
|---|---|---|
| `/`, `/index` | `index` | GET |
| `/add` | `add` | GET, POST |
| `/edit/<id>` | `edit` | GET, POST |
| `/delete/<id>` | `delete` | GET, POST |

Delete asks for confirmation rather than firing on a bare GET — the confirm page
posts back, so a link-prefetcher cannot wipe a row.

## Structure

```
app.py       Flask app + SQLAlchemy handle
models.py    Task
forms.py     TaskForm, DeleteForm
routes.py    the four views
templates/   base.html + one template per view
```
