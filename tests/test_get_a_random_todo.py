import unittest

from api_requests.dummy_jason_requests_todo import DummyJsonRequestsToDo


class TestGetRandomTodos(unittest.TestCase):

    def setUp(self):
        self.request_handler = DummyJsonRequestsToDo()

    def test_get_a_random_todo(self):
        response = self.request_handler.get_a_random_todo()
        expected_status_code = 200
        expected_status_msg = "OK"
        actual_response = response.reason
        expected_todo = response.json()
        todo = "todo"
        expected_completed = response.json()
        completed = "completed"
        expected_user_id = 51
        # expected_time = 5000
        # actual_time
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(expected_status_msg, actual_response)
        self.assertEquals(todo, expected_todo)
        self.assertEquals(completed, expected_completed)
        self.assertEquals(expected_user_id, response.json()["userId"])
        # self.assertEquals(expected_status_msg, response.json()["OK"])
