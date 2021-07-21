from django.urls import path
from . import views
urlpatterns = [
    path('', views.get, name="get"),
    path('post/<str:Title>', views.book_details, name="post")
]