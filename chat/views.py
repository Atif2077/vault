from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "chat/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "chat/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "chat/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            Person.objects.create(user=username)
            user.save()
        except IntegrityError:
            return render(request, "chat/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "chat/register.html")
    
def data(request):
    user = request.user
    global username
    username = user.username
    return username

def info():
    return "no"


@login_required(login_url="/login")
def index(request):
    return render(request, "chat/index.html", {
    })


def room(request):
    data = Chats.objects.all()
    name = Person.objects.get(user="no")
    return render(request, "chat/room.html", {
        "room_name": "chat",
        "data1": data,
        "name": name,
        })

def books(request):
    if request.method == "POST":
        value = request.POST.get("search")
        books = Books.objects.filter(title__contains = value)
        return render(request, "chat/books.html", {
        "books": books
    })
    
    books = Books.objects.all()
    return render(request, "chat/books.html", {
        "books": books
    })

def subjects(request):
    if request.method == "POST":
        u = request.user
        username = u.username
        subject_name = request.POST.get("subject_name")
        link = request.POST.get("link")
        student = request.POST.get("student")
        description = request.POST.get("description")
        Notes.objects.create(user=username, subject_name=subject_name, link=link, student=student, description=description)
        return HttpResponseRedirect(reverse("subjects"))
    
    b = Notes.objects.all().order_by("-time")
    return render(request, "chat/subjects.html", {
        "b": b
    })

def book_update(request):
    if request.method == "POST":
        u = request.user
        username = u.username
        book_name = request.POST.get("book_name")
        image_link = request.POST.get("image_link")
        book_link = request.POST.get("book_link")
        author = request.POST.get("author")
        Books.objects.create(user=username, title=book_name, link=book_link, image=image_link, author=author)
        return HttpResponseRedirect(reverse("books"))
    
    return render(request, "chat/book_update.html")

def assignment(request):
    if request.method == "POST":
        u = request.user
        username = u.username
        name = request.POST.get("assignment_name")
        deadline = request.POST.get("deadline")
        prof = request.POST.get("prof")
        Assignment.objects.create(user=username, name=name, time=deadline, prof=prof)
        return HttpResponseRedirect(reverse("assignment"))
    
    a = Assignment.objects.all().order_by("time")
    return render(request, "chat/assignment.html", {
        "a": a
    })