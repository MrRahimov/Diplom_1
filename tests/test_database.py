from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_available_buns_returns_list_of_buns():
    db = Database()
    buns = db.available_buns()
    assert all(isinstance(b, Bun) for b in buns)


def test_available_ingredients_returns_list_of_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert all(isinstance(i, Ingredient) for i in ingredients)
