from django.test import TestCase
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer


class PokemonSerializerTest(TestCase):

    def setUp(self):
        self.pokemon_data = {
            "nombre": "Pikachu",
            "tipo": "Eléctrico",
            "nivel": 5
        }
        self.pokemon = Pokemon.objects.create(**self.pokemon_data)
        self.serializer = PokemonSerializer(instance=self.pokemon)

    def test_contains_expected_fields(self):
        """
        Prueba que el serializador contiene los campos esperados.
        """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(
            ['id', 'nombre', 'tipo', 'nivel']))

    def test_field_content(self):
        """
        Prueba que los campos contienen el valor correcto.
        """
        data = self.serializer.data
        self.assertEqual(data['nombre'], "Pikachu")
        self.assertEqual(data['tipo'], "Eléctrico")
        self.assertEqual(data['nivel'], 5)
