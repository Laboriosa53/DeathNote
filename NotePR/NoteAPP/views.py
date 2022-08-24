from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
# Create your views here.

def note(request):
    note_list = Note.objects.all()
    return render(request, "NoteHTML/note.html",)   

def index(request):
    return render(request,"NoteHTML/index.html", )

def about(request):
    return render(request, "NoteHTML/about.html")    