"""Gravatar helper — a globally recognised avatar keyed on the email address."""
from hashlib import md5

from django import template

register = template.Library()


@register.filter(name="avatar")
def avatar(user, size: int = 40) -> str:
    """Return a Gravatar URL, falling back to a deterministic identicon."""
    seed = (user.email or user.get_username() or "").strip().lower()
    digest = md5(seed.encode("utf-8")).hexdigest()
    return f"https://www.gravatar.com/avatar/{digest}?s={size}&d=identicon&r=g"
