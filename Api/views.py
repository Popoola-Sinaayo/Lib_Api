from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from .models import Book
from .serializers import ApiSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def get(request):
    if request.method == "GET":
        book = Book.objects.all()
        book_api = ApiSerializer(book, many=True)
        return Response(book_api.data)
    elif request.method == "POST":
        returned = ApiSerializer(data=request.data)
        if returned.is_valid():
            returned.save()
            return Response(returned.data, status=status.HTTP_201_CREATED)
        return Response(returned.error(), status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_details(request, Title):
    try:
        book = Book.objects.get(Title=Title)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        sel_book = ApiSerializer(book)
        return Response(sel_book.data)
    elif request.method == 'PUT':
        sel_book = ApiSerializer(book, data=request.data)
        if sel_book.is_valid():
            sel_book.save()
            return Response(sel_book.data)
        return Response(sel_book.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sel_book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

