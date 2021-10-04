from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookForm
from .models import Author, Book
from django.template.response import TemplateResponse 

def fakehome(request):
    print("this is view")
    return HttpResponse("This is Home Page")

def exc(request):
    print('exception view')
    a = 10/0    
    return HttpResponse("This is exception page")

def user_info(request):
    print('User info view')
    context = {'name': 'Rahul'}

    return TemplateResponse('request', 'fake/user.html', context)

def create_book(request, pk):
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("detail-book", pk=book.id)
        else:
            return render(request, "partials/book_form.html", context={
                "form": form
            })

    context = {
        "form": form,
        "author": author,
        "books": books
    }

    return render(request, "fake/create_book.html", context)


def update_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(request.POST or None, instance=book)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("detail-book", pk=book.id)

    context = {
        "form": form,
        "book": book
    }

    return render(request, "partials/book_form.html", context)


def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == "POST":
        book.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def detail_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    context = {
        "book": book
    }
    return render(request, "partials/book_details.html", context)


def create_book_form(request):
    form = BookForm()
    context = {
        "form": form
    }
    return render(request, "partials/book_form.html", context)














# from django.shortcuts import redirect, render, get_object_or_404
# from .models import Author,Book
# from .forms import BookForm, BookFormSet
# from django.http import HttpResponse, HttpResponseNotAllowed


# def create_book(request,pk):
#     author = Author.objects.get(id=pk)
#     form = BookForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             book = form.save(commit=False)
#             book.save()
#             return redirect('detail-book', pk=book.id)
#         else:
#             return render(request, 'partials/book_form.', {
#                 "form":form,
#             })
    
    
#     context = {
#         "form": form,
#         "author": author,
#     }
#     # return render(request, 'fake/name.html',context)
#     return render(request, "create_book.html", context)


# # def create_book_forms(request):
# #     context = {
# #         "form": BookForm()
# #     }
# #     return render(request, 'partials/book_form.html', context)

# def update_book(request, pk):
#     book = Book.objects.get(id=pk)
#     form = BookForm(request.POST or None, instance=book)

#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect("detail-book", pk=book.id)

#     context = {
#         "form": form,
#         "book": book
#     }

#     return render(request, "partials/book_form.html", context)


# def delete_book(request, pk):
#     book = get_object_or_404(Book, id=pk)

#     if request.method == "POST":
#         book.delete()
#         return HttpResponse("")

#     return HttpResponseNotAllowed(
#         [
#             "POST",
#         ]
#     )    

# def details_book_forms(request,pk):
#     book = Book.objects.get(pk=pk)
#     context = {
#         "form": BookForm()
#     }
#     return render(request, 'partials/book_form.html', context)    