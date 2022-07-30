from django.http import JsonResponse
from .models import Drink
from .serializer import DrinkSerialializer


def drink_list(request):
    #get all the drinks
    #serialize them
    #return json
    drinks = Drink.objects.all()
    serializer =DrinkSerialializer(drinks, many=True)
    return JsonResponse({'drinks':serializer.data}, safe=False)