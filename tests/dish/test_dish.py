from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from models.ingredient import Ingredient


def test_dish():
    baiana = Dish('Fogazza Baiana', 12.00)
    baiana_too = Dish('Fogazza Baiana', 12.00)

    assert baiana.name == 'Fogazza Baiana'
    assert baiana == baiana_too
    assert hash(baiana) == hash(baiana_too)

    atum = Dish('Fogazza Atum', 14.00)

    assert hash(baiana) != hash(atum)
    assert baiana.__repr__() == "Dish('Fogazza Baiana', R$12.00)"

    baiana.add_ingredient_dependency(Ingredient('Azeitona'), 1)
    assert Ingredient('Azeitona') in baiana.get_ingredients()
    assert len(baiana.get_restrictions()) == 0

    with pytest.raises(TypeError):
        Dish('Fogazza Baiana', '12.00')
    with pytest.raises(ValueError):
        Dish('Fogazza Baiana', -12.00)
