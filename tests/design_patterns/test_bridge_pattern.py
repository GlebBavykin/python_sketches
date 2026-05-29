import pytest
from copy import deepcopy
from design_patterns.structural.bridge import Color, Circle, Rectangle, Shape


@pytest.mark.parametrize(
    "new_color",
    [
        Color.RED,
        Color.BLACK,
        Color.WHITE,
    ],
)
@pytest.mark.parametrize(
    "shape_instance",
    [
        Circle(radius=10),
        Rectangle(width=100, height=100),
    ],
)
def test_bridge_pattern(shape_instance: Shape, new_color: Color):
    """
    Test bridge pattern: Change color without creating a new shape instance
    """
    old_shape_instance = deepcopy(shape_instance)

    assert shape_instance.color != new_color
    assert new_color.__str__() not in shape_instance.__repr__()
    assert old_shape_instance.color == shape_instance.color

    shape_instance.color = new_color

    assert shape_instance.color == new_color
    assert new_color.__str__() in shape_instance.__repr__()
    assert old_shape_instance.color != shape_instance.color
