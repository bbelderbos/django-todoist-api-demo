from django.contrib import admin
from django.urls import path

from todos import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("completed/<int:todo_id>", views.complete_todo, name="complete_todo"),
]
