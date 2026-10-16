"""Template for GitHub OAuth sign-in.

    cp config/oauth_settings.example.py config/oauth_settings.py

Then create an OAuth app at https://github.com/settings/developers with:

    Homepage URL              http://127.0.0.1:8000
    Authorization callback    http://127.0.0.1:8000/oauth/complete/github/

Paste the pair below. `config/oauth_settings.py` is gitignored — never commit
real credentials. On a deployment target, enable "Force HTTPS" so the callback
scheme matches the registered one.
"""

SOCIAL_AUTH_GITHUB_KEY = ""
SOCIAL_AUTH_GITHUB_SECRET = ""
