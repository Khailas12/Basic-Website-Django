from django.shortcuts import render, redirect
from django.http import Http404
from .forms import BookForm
from .models import Book


def index(request):
    book = Book.objects.all()    
    context = {'book': book}
    return render(request, 'index.html', context)


def create(request):
    form = BookForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form = BookForm()
            return redirect('/')
    
        else:
            Http404
            
    context = {'form': form}
    return render(request, 'create.html', context)