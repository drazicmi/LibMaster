


from django.contrib import admin
from django.urls import path
from .views import  *

urlpatterns = [
    path('addBook/',add_book,name='add_book'),
    path('bookList', book_list, name='book_list'),
    path('addUser/', add_user, name='add_user'),
    path('deleteAllBooks', delete_all_books, name='deleteAllBooks'),
    path('', login_req, name='login'),
    path('logout/', logout_req, name='logout'),
    path('register/',registration, name='register'),
    path('addComment/',addComment, name='add_comment'),
    path('addCommentPage/<int:book_id>', addCommentPage, name='add_comment_page'),
    path('rateBook/', rateBook, name='rate_book'),
    path('rateBookPage/<int:book_id_rate>', rateBookPage, name='rate_book_page'),
    path('showCommentsForBook/',showCommentsForBook,name='show_comments_for_book'),
    path('sendRequest/', addRequest, name='addRequest'),
    path('showRequests/', showRequests, name='showRequests'),
    path('handleRequest/', handleRequest, name='handleRequest')

]