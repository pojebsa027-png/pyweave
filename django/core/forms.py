from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title", "body")
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "What happened?", "autofocus": True}),
            "body": forms.Textarea(attrs={"rows": 5, "placeholder": "Optional detail"}),
        }
