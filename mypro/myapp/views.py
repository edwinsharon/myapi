from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        person={
        'name':'edwin',
        'age':20,
        'gender':'male'
        }
        return Response(person)
    elif request.method == 'POST':
        return Response("method is post")
    elif request.method == 'PUT':
        return Response("method is put")
    

