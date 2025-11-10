import os
import sys
import pytest
from unittest.mock import Mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def bun():
    m = Mock()
    m.get_name.return_value = "Флюоресцентная булка R2-D3"
    m.get_price.return_value = 100.0
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
    m.get_price.return_value = 50.0
    return m
