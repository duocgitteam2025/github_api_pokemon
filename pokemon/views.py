from rest_framework import viewsets
from .models import Pokemon
from .serializers import PokemonSerializer
from django.http import JsonResponse


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


def health_check(request):
    """
    Health Check para verificar si la aplicación está corriendo correctamente.
    """
    return JsonResponse({"status": "ok"}, status=200)
