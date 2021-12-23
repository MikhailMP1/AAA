import Pizza
import pytest


def test_margo_recipe():
    expected = {'Margherita 🧀': 'tomato sauce, mozzarella, tomatoes'}
    assert expected == Pizza.Margherita('L').dict()
    assert expected == Pizza.Margherita('XL').dict()


def test_margo_size_eq():
    assert Pizza.Margherita('XL') == Pizza.Pepperoni('XL')
    assert Pizza.Hawaiian('XL') == Pizza.Pepperoni('XL')


def test_type():
    assert type(Pizza.Margherita('L').dict()) == dict

