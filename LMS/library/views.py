from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
# @login_required
# def books_view(request):
#     if request.method == 'POST':
#         if not request.user.has_perm('library.add_book'):
#             raise PermissionDenied
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(request.path)
#     else:
#         form = BookForm()
#     books = Book.objects.all()
#     return render(request, 'home.html', {'books': books, 'form': form})

def home(request):
    return render(request, 'home.html')

def addbook(request):
    return render(request,'add_book.html')