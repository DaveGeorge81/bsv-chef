import pytest
import unittest.mock as mock #Load the mocking library
from src.controllers.recipecontroller import RecipeController

# add your test case implementation here
@pytest.mark.unit
def test():
    controller = mock.MagicMock() #Mock the dependency
    sut = RecipeController(controller)

    recipies = sut.load_recipes()
    assert len(recipies) == 3