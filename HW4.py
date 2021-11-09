import json


class ColorizeMixin:

    repr_color_code = 32

    def colorize(self, repr_color_code):
        return f"\033[1;{repr_color_code};40m {self.__repr__()}  \n"


class Advert(ColorizeMixin, dict):

    def __getattr__(self, value):
        if not isinstance(self[value], dict):
            return self[value]
        else:
            return Advert(self[value])

    @property
    def price(self):
        if self.get('price', 0) < 0:
            return 'ValueError: must be >= 0'
        else:
            return self.get('price', 0)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    lesson_str = """{
                    "title": "python",
                    "price": 0,
                    "location": {
                    "address": "город Москва, Лесная, 7",
                    "metro_stations": ["Белорусская"]
                    }
                    }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    print(lesson_ad.price)
    print(lesson_ad.location.address)
    print(lesson_ad.colorize(repr_color_code=32))

    iphone = {
        "title": "iPhone X",
        "price": -1,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }
    iphone_ad = Advert(iphone)
    print(iphone_ad.price)
    print(iphone_ad.location.address)
    print(iphone_ad.colorize(repr_color_code=37))
