from django.contrib import admin
from django.urls import path

from accounts import views

from .views import (
    create_book,
    create_book_form,
    detail_book,
    update_book,
    delete_book,
    fakehome,
    exc,
    user_info,

)


urlpatterns = [
    path('<pk>/', create_book, name='create-book'),
    path('htmx/book/<pk>/', detail_book, name="detail-book"),
    path('htmx/book/<pk>/update/', update_book, name="update-book"),
    path('htmx/book/<pk>/delete/', delete_book, name="delete-book"),
    path('htmx/create-book-form/', create_book_form, name='create-book-form'),
    path('middile/', fakehome, name="fakehome"),
    path('exc/', exc, name="exception"),
    path('user/', user_info, name="user")
]








# from django.urls.resolvers import URLPattern

# from accounts import views
# from django.urls.conf import path
# from fake import views
# from .views import (
#     create_book,
#     # create_book_forms,
#     details_book_forms,
#     update_book,
#     delete_book,
# )


# # urlpatterns = [
# #     path('new', views.create_book, name="new"),
# #     path('<pk>/', views.create_book, name="new"),
# #     path('htmx/book-form', views.create_book_forms, name='book-form'),
# #     path('htmx/detail/<pk>/', views.details_book_forms, name='detail-book'),
# # ]


# urlpatterns = [
#     path('<pk>/', create_book, name='create-book'),
#     path('htmx/book/<pk>/', details_book_forms, name="detail-book"),
#     path('htmx/book/<pk>/update/', update_book, name="update-book"),
#     path('htmx/book/<pk>/delete/', delete_book, name="delete-book"),
#     # path('htmx/create-book-form/', create_book_forms, name='create-book-form'),
# ]