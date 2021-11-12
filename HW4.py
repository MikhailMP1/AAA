import json


class ColorizeMixin:
    """ Определяет цвет вывода метода repr в классе Advert."""

    repr_color_code = 32

    def colorize(self, repr_color_code):
        return f"\033[1;{repr_color_code};40m {self.__repr__()}  \033[1;37;40m "


class Advert(ColorizeMixin, dict):
    """Динамичесĸи создает атрибуты эĸземпляра ĸласса из атрибутов JSON-объеĸта.
       Позволяет обращаться к ним через точку."""

    def __getattr__(self, value):
        if not isinstance(self[value], dict):
            return self[value]
        else:
            return Advert(self[value])

    @property
    def price(self):

        """проверяет, что устанавливаемое значение цены не отрицательное.
            В случае отсутствия возвращает 0."""

        if self.get('price', 0) < 0:
            return 'ValueError: must be >= 0'
        else:
            return self.get('price', 0)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    lesson_str = """{
                    "title": "iPhone X",
                    "price": 100,
                    "location": {
                    "address": "город Самара, улица Мориса Тореза, 50",
                    "metro_stations": ["Спортивная", "Гагаринская"]
                    }
                    }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    print(lesson_ad.colorize(repr_color_code=33))
    print(lesson_ad.price)
    print(lesson_ad.location.address)
