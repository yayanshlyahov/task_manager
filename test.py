import json
from app import app
from model import get_task
from factories import create_task_with_data
import unittest
import pytest
from model import Task


@pytest.fixture(scope='function')
def client():
    return app.test_client()


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


@pytest.fixture
def fixture():
    print('KEK')


@pytest.mark.parametrize(
    'a, b, c', (
        (1, 2, 3),
        (1, 2, 5),
    )
)
def test_passing(a, b, c, fixture):
    fixture
    assert (a, b, c) == (a, b, c)


def test_client(client):
    response = client.get('/', content_type='html/text')
    assert response.status_code == 200
    assert response.data == b'Hello world'


@pytest.mark.parametrize(
    'name, password, yo', (
        ('some name', 'some password', 123),
        ('some name', 's'*100, 123),
        ('s'*100, 'sadsfasdf', 123),
        ('s'*100, 'sadsfasdf', 9*9*9),
    )
)
def test_client_create_user(name, password, yo, client):
    data = {
        'name': name,
        'password': password,
        'yo': yo
    }
    response = client.post('/api/user/', json=json.dumps(data))
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'name, description', (
        ('new task', 'new descritpion'),
        ('new task', 'n'*100),
    )
)
def test_client_create_task_api(name, description, client):
    data = {
        'name': name,
        'description': description,
        'user_id': 1
    }
    response = client.post('/api/task/', json=json.dumps(data))
    assert response.status_code == 200
    task_object = Task.query.all()[-1]
    assert task_object.name == data['name']
    assert task_object.description == data['description']


if __name__ == '__main__':
    unittest.main()
