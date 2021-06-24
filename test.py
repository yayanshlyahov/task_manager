from app import app
from model import get_task
from factories import create_task_with_data
import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello world')


class TestTask(unittest.TestCase):

    def test_create_task(self):
        initial_count = len(get_task())
        create_task_with_data()
        final_count = len(get_task())
        assert initial_count + 1 == final_count

    def test_create_task_with_name(self):
        create_task_with_data(new_name='new_task_name')
        final_count = len(
            [task for task in get_task() if task['name'] == 'new_task_name']
        )
        assert final_count >= 1


if __name__ == '__main__':
    unittest.main()
