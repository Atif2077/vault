from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chat", views.room, name="room"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("notes", views.subjects, name="subjects"),
    path("books", views.books, name="books"),
    path("book_update", views.book_update, name="book_update"),
    path("assignment", views.assignment, name="assignment"),
]
