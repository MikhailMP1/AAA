from abc import ABC, abstractmethod
import random


class AnimeMon(ABC):
    @abstractmethod
    def inc_exp(self, value: int):
        pass

    @property
    @abstractmethod
    def exp(self):
        pass


class Pokemon(AnimeMon):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self._exp = 0

    def inc_exp(self, value: int):
        self._exp += value

    @property
    def exp(self):
        return self._exp


class Digimon(AnimeMon):
    def __init__(self, name: str):
        self.name = name
        self._exp = 0

    def inc_exp(self, value: int):
        self._exp += value * 8

    @property
    def exp(self):
        return self._exp


def train(mon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - mon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            mon.inc_exp(step_size)
