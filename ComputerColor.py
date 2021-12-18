from abc import ABC


class ComputerColor(ABC):

    def __repr__(self):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass


class Colors(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red_level, green_level, blue_level):
        self.red_level = red_level
        self.green_level = green_level
        self.blue_level = blue_level

    def __str__(self):
        return f'{self.START};{self.red_level};{self.green_level};{self.blue_level}{self.MOD}●{self.END}{self.MOD}'

    __repr__ = __str__

    def __eq__(self, other):
        if not isinstance(other, Colors):
            return False
        return (
                self.red_level == other.red_level
                and self.green_level == other.green_level
                and self.blue_level == other.blue_level
        )

    def __add__(self, other):
        if not isinstance(other, Colors):
            return False
        return Colors(
            min(255, self.red_level + other.red_level),
            min(255, self.green_level + other.green_level),
            min(255, self.blue_level + other.blue_level)
        )

    def __hash__(self):
        return hash((self.red_level, self.green_level, self.blue_level))

    def __mul__(self, contrast):
        cl = -256 * (1 - contrast)
        factor = (259 * (cl + 255)) / (255 * (259 - cl))
        return Colors(int(factor*(self.red_level-128)+128),
                      int(factor*(self.red_level-128)+128),
                      int(factor*(self.red_level-128)+128)
                      )

    __rmul__ = __mul__


class HSBColor(ComputerColor):
    pass


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
        ]
    for row in a_matrix:
        print("".join(str(ptr) for ptr in row))


if __name__ == "__main__":
    red = ComputerColor()
    green = Colors(0, 255, 0)
    blue = Colors(0, 0, 255)

    print_a(0.5 * (green + blue))
