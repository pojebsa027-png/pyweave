# PyWeave

Two reference implementations of the same idea — a small notes/tasks web app —
one in **Django**, one in **Flask**. Built as a teaching ladder: each Flask
directory adds exactly one concept, each Django directory is a production-shaped
project layout.

Nothing here is a toy stub. Every app boots, every route renders, every model
migrates.

```
pyweave/
├── django/                 Django 5 project — project package `config`, app `core`
│   ├── config/             settings, urls, asgi/wsgi
│   ├── core/               models, views, forms, templates, static
│   └── manage.py
├── flask/                  Flask 3 ladder — ten steps, one concept each
│   ├── 01-minimal-app/
│   ├── 02-html-templates/
│   ├── 03-layouts/
│   ├── 04-forms/
│   ├── 05-post-requests/
│   ├── 06-database/
│   ├── 07-crud/
│   ├── 08-bootstrap/
│   ├── 09-edit/
│   └── 10-taskapp/         the finished one — add / edit / delete / flash
├── docs/                   architecture notes
└── .github/workflows/      CI for both stacks
```

## Quickstart — Django

```bash
cd django
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin/
python manage.py runserver
```

→ http://127.0.0.1:8000/

## Quickstart — Flask

```bash
cd flask/10-taskapp
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python app.py
```

→ http://127.0.0.1:5000/

## Configuration

| Variable | Default | Used by |
|---|---|---|
| `DJANGO_SECRET_KEY` | dev placeholder | Django |
| `DJANGO_DEBUG` | `1` | Django |
| `DJANGO_ALLOWED_HOSTS` | `*` | Django |
| `SECRET_KEY` | dev placeholder | Flask (form CSRF) |

GitHub sign-in on the Django side is opt-in and off by default — copy
`django/config/oauth_settings.example.py` to `oauth_settings.py`, fill in a real
OAuth app pair, and reinstall with the `social-auth-app-django` extra.

## Layout convention

- Flask steps are numbered because they are meant to be read in order.
- Django uses a single app, `core`, because the point of that side is layout,
  not feature count.

## License

MIT — see [LICENSE](LICENSE).
