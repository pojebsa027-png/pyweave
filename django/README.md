# django/

Django 5 project. Project package is `config`, the only app is `core`.

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Routes

| Path | Name | View |
|---|---|---|
| `/` | `core:home` | `HomeView` — lists notes |
| `/notes/new/` | `core:note-create` | `NoteCreateView` |
| `/accounts/login/` | `login` | `django.contrib.auth` |
| `/accounts/logout/` | `logout` | `django.contrib.auth` (POST) |
| `/admin/` | — | Django admin |

## Environment

| Variable | Default |
|---|---|
| `DJANGO_SECRET_KEY` | dev placeholder |
| `DJANGO_DEBUG` | `1` |
| `DJANGO_ALLOWED_HOSTS` | `*` |

## Optional GitHub sign-in

```bash
cp config/oauth_settings.example.py config/oauth_settings.py
# fill in SOCIAL_AUTH_GITHUB_KEY / SOCIAL_AUTH_GITHUB_SECRET
pip install social-auth-app-django
```

`config/oauth_settings.py` is gitignored. When present, `settings.py` appends
`social_django` to `INSTALLED_APPS`, its middleware to `MIDDLEWARE`, its context
processors to `TEMPLATES`, and `GithubOAuth2` to `AUTHENTICATION_BACKENDS`, then
mounts `/oauth/` in the root URLconf.
