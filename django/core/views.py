from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import NoteForm
from .models import Note

LOCAL_HOSTS = ("localhost", "127.0.0.1", "[::1]")


class HomeView(ListView):
    model = Note
    template_name = "core/home.html"
    context_object_name = "notes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["islocal"] = self.request.get_host().startswith(LOCAL_HOSTS)
        context["app_name"] = settings.APP_NAME
        return context


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "core/note_form.html"
    success_url = reverse_lazy("core:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = settings.APP_NAME
        return context
