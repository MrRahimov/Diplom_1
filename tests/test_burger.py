import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.fixture
def bun():
    m = Mock()
    m.get_name.return_value = "Флюоресцентная булка R2-D3"
    return m

@pytest.fixture
def meat():
    m = Mock()
    m.get_name.return_value = "Мясо бессмертного моллюска Protostomia"
    m.get_price.return_value = 1337.0
    return m

@pytest.fixture
def sauce():
    m = Mock()
    m.get_name.return_value = "Соус Spicy X"
    m.get_price.return_value = 100.0
    return m

def test_burger_starts_empty():
    b = Burger()
    assert b.ingredients == []

@pytest.mark.parametrize("bun_price", [50.0, 100.0, 199.99])
def test_set_buns_affects_price(bun, meat, bun_price):
    b = Burger()
    bun.get_price.return_value = bun_price
    b.set_buns(bun)
    b.add_ingredient(meat)
    assert b.get_price() == pytest.approx(2*bun_price + 1337.0, rel=1e-6)

def test_add_and_remove_ingredient(bun, meat, sauce):
    b = Burger()
    bun.get_price.return_value = 100.0
    b.set_buns(bun)
    b.add_ingredient(meat)
    b.add_ingredient(sauce)
    assert len(b.ingredients) == 2
    b.remove_ingredient(0)
    assert [i.get_name() for i in b.ingredients] == ["Соус Spicy X"]

def test_move_ingredient(bun, meat, sauce):
    b = Burger()
    bun.get_price.return_value = 100.0
    b.set_buns(bun)
    b.add_ingredient(meat)   # idx 0
    b.add_ingredient(sauce)  # idx 1
    b.move_ingredient(1, 0)
    assert [i.get_name() for i in b.ingredients] == [
        "Соус Spicy X", "Мясо бессмертного моллюска Protostomia"
    ]

def test_receipt_contains_names_and_total(bun, meat):
    b = Burger()
    bun.get_price.return_value = 80.0
    b.set_buns(bun)
    b.add_ingredient(meat)
    receipt = b.get_receipt()
    assert "Флюоресцентная булка R2-D3" in receipt
    assert "Мясо бессмертного моллюска Protostomia" in receipt
    assert str(b.get_price()) in receipt
