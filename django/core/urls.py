from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("notes/new/", views.NoteCreateView.as_view(), name="note-create"),
]
