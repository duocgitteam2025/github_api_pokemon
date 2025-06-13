from django.test import TestCase

from pokemon.models import Pokemon


class PokemonModelTest(TestCase):

    def setUp(self):
        """
        Método que se ejecuta antes de cada test.
        """
        self.pokemon = Pokemon.objects.create(
            nombre="Pikachu", tipo="Eléctrico", nivel=5
        )

    def test_pokemon_creation(self):
        """
        Prueba que un Pokémon se cree correctamente en la base de datos.
        """
        self.assertEqual(self.pokemon.nombre, "Pikachu")
        self.assertEqual(self.pokemon.tipo, "Eléctrico")
        self.assertEqual(self.pokemon.nivel, 5)

    def test_pokemon_str_method(self):
        """
        Prueba el método __str__ del modelo.
        """
        self.assertEqual(str(self.pokemon), "Pikachu")
