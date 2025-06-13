from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from pokemon.models import Pokemon


class PokemonViewSetTest(APITestCase):

    def setUp(self):
        self.pokemon = Pokemon.objects.create(
            nombre="Pikachu", tipo="Eléctrico", nivel=5
        )

    def test_list_pokemon(self):
        """
        Prueba el listado de Pokémon.
        """
        url = reverse("pokemon-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_pokemon(self):
        """
        Prueba el detalle de un Pokémon.
        """
        url = reverse("pokemon-detail", args=[self.pokemon.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nombre"], "Pikachu")
