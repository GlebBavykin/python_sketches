import pytest
from _pytest.fixtures import SubRequest

from algorithms.tower_of_hanoi import TowerOfHanoi, solve_hanoi


@pytest.fixture(scope="function")
def disk_numbers(request: SubRequest) -> int:
    """
    Number of disks in Tower of Hanoi puzzle
    """
    return request.param


@pytest.fixture(scope="function")
def tower(disk_numbers: int) -> TowerOfHanoi:
    """
    The tower of hanoi instance
    """
    tower = TowerOfHanoi()
    for disk in reversed(range(1, disk_numbers + 1)):
        tower.a.append(disk)
    return tower


@pytest.mark.parametrize("disk_numbers", [1, 2, 3, 4, 5, 6, 7, 8, 9], indirect=True)
def test_resolve_tower_of_hanoi(tower: TowerOfHanoi, disk_numbers: int) -> None:
    """
    Solve the Tower of Hanoi puzzle,
        - move a stack of disks from a Source rod to a Destination rod using an Auxiliary (temporary) rod:
            - move only one disk at a time,
            - never place a larger disk on top of a smaller one
    """
    solve_hanoi(tower)
    assert len(tower.a) == 0
    assert len(tower.c) == disk_numbers
