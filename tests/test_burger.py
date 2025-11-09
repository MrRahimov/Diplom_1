import pytest
from praktikum.burger import Burger


def test_init_creates_empty_ingredients():
    burger = Burger()
    assert burger.ingredients == []


def test_set_buns_sets_bun(bun):
    burger = Burger()
    burger.set_buns(bun)
    assert burger.bun == bun


def test_add_ingredient_appends_to_ingredients(bun, meat):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(meat)
    assert burger.ingredients == [meat]


def test_remove_ingredient_removes_by_index(bun, meat, sauce):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(meat)
    burger.add_ingredient(sauce)

    burger.remove_ingredient(0)

    assert burger.ingredients == [sauce]


def test_move_ingredient_changes_order(bun, meat, sauce):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(meat)   # index 0
    burger.add_ingredient(sauce)  # index 1

    burger.move_ingredient(1, 0)

    assert burger.ingredients == [sauce, meat]


@pytest.mark.parametrize("bun_price", [50.0, 100.0, 199.99])
def test_get_price_uses_bun_and_ingredients(bun, meat, bun_price):
    bun.get_price.return_value = bun_price

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(meat)

    expected = 2 * bun_price + meat.get_price.return_value
    assert burger.get_price() == pytest.approx(expected)


def test_get_receipt_contains_bun_names(bun, meat):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(meat)

    receipt = burger.get_receipt()

    assert bun.get_name.return_value in receipt


def test_get_receipt_contains_ingredient_name(bun, meat):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(meat)

    receipt = burger.get_receipt()

    assert meat.get_name.return_value in receipt


def test_get_receipt_contains_total_price(bun, meat):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(meat)

    total = 2 * bun.get_price.return_value + meat.get_price.return_value
    receipt = burger.get_receipt()

    assert str(total) in receipt
