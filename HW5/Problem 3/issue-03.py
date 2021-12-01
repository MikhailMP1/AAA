from typing import List, Tuple
import unittest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TestTF(unittest.TestCase):
    def test_tf(self):
        actual = fit_transform('Sas', 'Sos', 'Kek', 'Lol')
        expected = [('Sas', [0, 0, 0, 1]), ('Sos', [0, 0, 1, 0]), ('Kek', [0, 1, 0, 0]), ('Lol', [1, 0, 0, 0])]

        self.assertEqual(actual, expected)

    def test_absence(self):
        actual = fit_transform('Moscow', 'London', 'New York')
        expected = [('Paris', [1])]

        self.assertNotIn(actual, expected)

    def test_presence(self):
        actual = fit_transform('Moscow', 'London', 'New York')
        expected = ('Moscow', [0, 0, 1])

        self.assertIn(expected, actual)

    def test_instance(self):
        actual = fit_transform('Moscow', 'London', 'New York')
        expected = list

        self.assertIsInstance(actual, expected)

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()


if __name__ == '__main__':
    unittest.main()
