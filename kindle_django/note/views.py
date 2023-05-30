from .forms import NoteForm
from django.shortcuts import render
from .models import Note
from django.shortcuts import get_object_or_404, render, redirect

def index(request):
  note_list = Note.objects.all()
  return render(request, "note/index.html", {'note_list': note_list})

def show(request,pk):
    note = get_object_or_404(Note,pk=pk)
    return render(request,"note/show.html",{'note':note})

def create(request):
    form = NoteForm
    return render(request,"note/create.html",{'form':form})

def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        form.save()
        return redirect('note_list')
    else:
        form = NoteForm
        return render(request,"note/create.html",{'form':form})

