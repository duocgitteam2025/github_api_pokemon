from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pokemon.views import PokemonViewSet

router = routers.DefaultRouter()
router.register(r'pokemon', PokemonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('pokemon/', include('pokemon.urls')),

]
