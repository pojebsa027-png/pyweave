# Architecture

## Why two stacks in one repo

The Django side and the Flask side answer different questions.

- **Flask** answers *"what is the smallest change that adds this concept?"*
  Ten directories, each one a complete runnable app, each one adding a single
  idea on top of the previous.
- **Django** answers *"what does a real project layout look like?"* One project
  package, one app, settings driven by environment variables, a migration that
  ships, tests that pass.

They share no code on purpose. Importing one from the other would blur exactly
the comparison the repo exists to make.

## Django layout

```
config/          project package — the thing `manage.py` points at
  settings.py    env-driven; OAuth block appended conditionally
  urls.py        root URLconf, mounts core + admin + auth
  asgi.py        async entrypoint
  wsgi.py        sync entrypoint
core/            the only app
  models.py      Note
  views.py       HomeView (ListView), NoteCreateView (CreateView)
  forms.py       NoteForm (ModelForm)
  urls.py        app_name = "core" — reverse as core:home
  context_processors.py   injects app_name / oauth_enabled
  templatetags/avatars.py gravatar filter
  templates/     base.html + core/ + registration/
  static/        site.css, favicon.ico
```

The OAuth wiring lives in a single conditional block at the bottom of
`settings.py`. If `config/oauth_settings.py` is absent — the default — nothing
about social auth is loaded: no app, no middleware, no backend, no context
processors. That keeps the dependency out of `requirements.txt` unless you ask
for it.

## Flask ladder

| Step | Adds |
|---|---|
| 01-minimal-app | a route and a string |
| 02-html-templates | `render_template`, a value passed to the view |
| 03-layouts | template inheritance, a second page |
| 04-forms | Flask-WTF, CSRF, a validated form |
| 05-post-requests | reading `form.validate_on_submit()` |
| 06-database | Flask-SQLAlchemy, the `Task` model, `db.create_all()` |
| 07-crud | list + create against the database |
| 08-bootstrap | a real page shell |
| 09-edit | update an existing row |
| 10-taskapp | delete, flash messages, a README, pinned deps |

Steps 01–05 keep their templates inline so the diff between steps is the only
thing you have to read.

## Data model

Both stacks model the same two fields: a short title and a creation timestamp.
Django's `Note` adds an optional body; Flask's `Task` does not. The divergence is
deliberate — it shows where a `ModelForm` earns its keep versus a plain
`FlaskForm`.
