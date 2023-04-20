from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
# from tests.mocks import ingredients


def test_ingredient():
    salt = Ingredient('sal')
    salt_2 = Ingredient('sal')

    assert salt.__repr__() == "Ingredient('sal')"
    assert salt.__eq__(salt_2)
    assert salt.__hash__() == salt_2.__hash__()
    assert salt.name == 'sal'
    assert len(salt.restrictions) == 0


    water = Ingredient('água')

    assert salt.__hash__() != water.__hash__()
