from django.test import SimpleTestCase
from django.urls import resolve, reverse

from pokemon.views import PokemonViewSet


class TestUrls(SimpleTestCase):

    def test_pokemon_list_url(self):
        """
        Prueba la URL del listado de Pokémon.
        """
        url = reverse("pokemon-list")
        self.assertEqual(resolve(url).func.cls, PokemonViewSet)

    def test_pokemon_detail_url(self):
        """
        Prueba la URL del detalle de un Pokémon.
        """
        url = reverse("pokemon-detail", args=[1])
        self.assertEqual(resolve(url).func.cls, PokemonViewSet)
