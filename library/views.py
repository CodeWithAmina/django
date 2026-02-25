from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

@login_required(login_url='login')
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

@login_required(login_url='login')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'books': Book.objects.all()})
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
    
