from collections import deque

from pydantic import BaseModel, ConfigDict, Field


class HanoiStack(deque):
    def append(self, disk: int):
        """
        Append a disk to the top of the stack, but never place a larger disk on top of a smaller one
        """
        if self and self[-1] < disk:
            raise ValueError(f"Cannot place larger disk {disk} on top of smaller disk {self[-1]}")
        super().append(disk)


class TowerOfHanoi(BaseModel):
    """
    Data model for tower_of_hanoi
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)
    a: HanoiStack = Field(default_factory=HanoiStack, alias="source")
    b: HanoiStack = Field(default_factory=HanoiStack, alias="auxiliary")
    c: HanoiStack = Field(default_factory=HanoiStack, alias="destination")


def move(src: HanoiStack, dst: HanoiStack) -> None:
    """
    Helper function to move a disk from the source to the destination
    """
    disk = src.pop()
    dst.append(disk)


def solve_hanoi(tower: TowerOfHanoi) -> None:
    """
    Solve a tower of hanoi recursively
    """

    def _solve(n: int, src: HanoiStack, dst: HanoiStack, aux: HanoiStack) -> None:
        if n == 0:
            return
        _solve(n - 1, src, aux, dst)
        move(src, dst)
        _solve(n - 1, aux, dst, src)

    _solve(n=len(tower.a), src=tower.a, dst=tower.c, aux=tower.b)
