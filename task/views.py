from django.shortcuts import render
from .serializer import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def first_task(request) :
    return render(request , "index.html")


def view_category(request) : 


    return render(request , "view_category.html")

@api_view(['GET'])
def apiCategory(request):
    category = Category.objects.all()
    