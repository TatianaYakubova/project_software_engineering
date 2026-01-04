import unittest
from app2 import app2  # Импортируем приложение из файла app.py

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app2.test_client()  # Создаем клиент для тестирования
        self.app.testing = True  # Включаем режим тестирования

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Hello World!')

    def test_sum_valid(self):
        response = self.app.get('/sum?a=2&b=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '5.0')

    def test_sum_invalid(self):
        response = self.app.get('/sum?a=two&b=three')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Введите корректные числа')

if __name__ == '__main__':
    unittest.main()