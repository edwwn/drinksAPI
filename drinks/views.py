from pickle import GET
from urllib import response
from wsgiref.util import request_uri
from django.http import JsonResponse
from .models import Drink
from .serializer import DrinkSerialializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
    #get all the drinks
    #serialize them
    #return json
    
    if request.method == 'GET':   
        drinks = Drink.objects.all()
        serializer =DrinkSerialializer(drinks, many=True)
        return JsonResponse({'drinks':serializer.data}, safe=False)
    
    if request.method == 'POST':
        serializer =DrinkSerialializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)