"""
Задачи из книги. --Глава 11. Тестирование.
"""
import unittest
from education_files.for_testing import normal_name_format


class NameTestCase(unittest.TestCase):
    """Тесты для normal_name_format"""

    def test_first_last_names(self):
        """Имена из 2 составляющих работают нормально?"""
        format_names = normal_name_format('foxy', 'WRTH')
        self.assertEqual(format_names, 'Foxy Wrth')

    def test_first_last_middle_names(self):
        """Имена из 3 составляющих работают нормально?"""
        format_names = normal_name_format('foxy', 'FX', 'WRTH')
        self.assertEqual(format_names, 'Foxy Wrth Fx')


if __name__ == '__main__':
    unittest.main()
    unittest.main()
