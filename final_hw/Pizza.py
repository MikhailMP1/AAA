from random import randint, choice
import click


class Margherita:
    """ Описывает возможные размеры и состав пиццы 'Маргарита' """
    def __init__(self, size):
        if size in ('L', 'XL'):
            self.size = size
        else:
            ValueError('Sorry, this size is not available')

    @staticmethod
    def dict():
        recipe = {'Margherita 🧀': 'tomato sauce, mozzarella, tomatoes'}
        return recipe

    def __eq__(self, other):
        return self.size == other.size


class Pepperoni:
    """ Описывает возможные размеры и состав пиццы 'Пепперони' """
    def __init__(self, size):
        if size in ('L', 'XL'):
            self.size = size
        else:
            ValueError('Sorry, this size is not available')

    @staticmethod
    def dict():
        recipe = {'Pepperoni 🍕': 'tomato sauce, mozzarella, pepperoni'}
        return recipe

    def __eq__(self, other):
        return self.size == other.size


class Hawaiian:
    """ Описывает возможные размеры и состав пиццы 'Гавайская' """
    def __init__(self, size):
        if size in ('L', 'XL'):
            self.size = size
        else:
            ValueError('Sorry, this size is not available')

    @staticmethod
    def dict():
        recipe = {'Hawaiian 🍍': 'tomato sauce, mozzarella, chicken, pineapple'}
        return recipe

    def __eq__(self, other):
        return self.size == other.size


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', default='L', type=str)
@click.argument('pizza', nargs=1)
def order(pizza: str, size: str, deliver: bool):
    """Готовит и доставляет пиццу"""
    if pizza == 'Pepperoni':
        Pepperoni(size)
    elif pizza == 'Margherita':
        Margherita(size)
    elif pizza == 'Hawaiian':
        Hawaiian(size)
    print(f' 👨🏻‍🍳 Приготовили за {randint(1,10)}с!')
    if deliver:
        print(f' 🛵 Доставили за {randint(1,10)}с!')


@cli.command()
def menu():
    """Выводит меню"""
    sizes = ['L', 'XL']
    print(Margherita(choice(sizes)).dict())
    print(Pepperoni(choice(sizes)).dict())
    print(Hawaiian(choice(sizes)).dict())


def log(my_str: str = None):
    """ Возвращает случайное время выполнения функции ,либо подставляет его в указанное место"""
    def decorate(func):
        def decor(*args, **kwargs):
            if my_str is None:
                func(*args, **kwargs)
                print(f'{func.__name__} - {randint(1,10)} c!')
            else:
                func(*args, **kwargs)
                print(my_str.replace('{}', str(randint(1, 10))))
        return decor

    return decorate


@log()
def bake(pizza):
    """Готовит пиццу"""


@log('Доставили за {}с!')
def delivery(pizza):
    """Доставляет пиццу"""


@log('Забрали за {}с!')
def pickup(pizza):
    """Самовывоз"""


if __name__ == '__main__':
    print(bake(Margherita('L')))
    print(delivery(Margherita('L')))
