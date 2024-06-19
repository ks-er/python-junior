from django.test import RequestFactory, TestCase


class MiddlewareTestCase(TestCase):

    @classmethod
    def test_FormatterMiddleware(cls):
        response = cls.client.get('/calc/?maths=3*3;10-2;12/5&delimiter=;')
        content = response.content.decode()
        cls.assertEqual(content, '<p>3*3 = 9</p><p>10-2 = 8</p><p>12/5 = 2.4</p>')

    @classmethod
    def test_default_FormatterMiddleware(cls):
        response = cls.client.get('/calc/?maths=300*30,1-2,100/5')
        content = response.content.decode()
        cls.assertEqual(content, '<p>300*30 = 9000</p><p>1-2 = -1</p><p>100/5 = 20.0</p>')

    @classmethod
    def test_CheckErrorMiddleware(cls):
        response = cls.client.get('/calc/?maths=3*3;10-2;12/0&delimiter=;')
        content = response.content.decode().split(':')[0]

        cls.assertEqual(content, 'Ошибка')

    @classmethod
    def test_default_CheckErrorMiddleware(cls):
        response = cls.client.get('/calc/?maths=3*3;10-2;12/5')
        content = response.content.decode().split(':')[0]

        cls.assertEqual(content, 'Ошибка')