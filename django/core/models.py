from django.db import models
from django.urls import reverse


class Note(models.Model):
    """A single short note. The whole persistence layer of this demo."""

    title = models.CharField(max_length=120)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("core:home")
