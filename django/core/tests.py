from django.test import TestCase
from django.urls import reverse

from .models import Note


class HomeViewTests(TestCase):
    def test_empty_state_renders(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nothing here yet")

    def test_notes_are_listed_newest_first(self):
        Note.objects.create(title="older")
        Note.objects.create(title="newer")
        response = self.client.get(reverse("core:home"))
        titles = [n.title for n in response.context["notes"]]
        self.assertEqual(titles, ["newer", "older"])

    def test_rejects_non_local_host_as_remote(self):
        response = self.client.get(reverse("core:home"), HTTP_HOST="example.com")
        self.assertFalse(response.context["islocal"])


class NoteCreateViewTests(TestCase):
    def test_create_redirects_home(self):
        response = self.client.post(
            reverse("core:note-create"),
            {"title": "shipped", "body": "with a body"},
        )
        self.assertRedirects(response, reverse("core:home"))
        self.assertTrue(Note.objects.filter(title="shipped").exists())

    def test_blank_title_is_rejected(self):
        response = self.client.post(reverse("core:note-create"), {"title": "", "body": ""})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context["form"], "title", "This field is required.")
