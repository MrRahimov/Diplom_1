import pytest
from praktikum.burger import Burger


def test_burger_starts_empty():
    burger = Burger()
    assert burger.ingredients == []


@pytest.mark.parametrize("bun_price", [50.0, 100.0, 199.99])
def test_set_buns_affects_price(bun, meat, bun_price):
    bun.get_price.return_value = bun_price
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(meat)

    expected = 2 * bun_price + meat.get_price.return_value
    assert burger.get_price() == pytest.approx(expected)


def test_add_and_remove_ingredient(bun, meat, sauce):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(meat)
    burger.add_ingredient(sauce)

    assert len(burger.ingredients) == 2

    burger.remove_ingredient(0)
    assert [i.get_name() for i in burger.ingredients] == [
        sauce.get_name.return_value
    ]


def test_move_ingredient(bun, meat, sauce):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(meat)   
    burger.add_ingredient(sauce)  

    burger.move_ingredient(1, 0)

    assert [i.get_name() for i in burger.ingredients] == [
        sauce.get_name.return_value,
        meat.get_name.return_value,
    ]


def test_receipt_contains_names_and_total(bun, meat):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(meat)

    receipt = burger.get_receipt()
    total = 2 * bun.get_price.return_value + meat.get_price.return_value

    assert bun.get_name.return_value in receipt
    assert meat.get_name.return_value in receipt
    assert str(total) in receipt
