import time
import unittest

from api_requests.dummy_jason_requests_todo import DummyJsonRequestsToDo


class TestGetALimitAndSkipTodos(unittest.TestCase):

    def setUp(self):
        self.request_handler = DummyJsonRequestsToDo()

    def test_get_limit_and_skip_todos(self):
        start_time = time.time()
        response = self.request_handler.get_a_limit_and_skip_todos(limit=3, skip=10)
        end_time = time.time()
        expected_status_code = 200
        expected_status_msg = "OK"
        actual_response = response.reason
        expected_limit = 3
        expected_time = 5000
        actual_time = (end_time-start_time)*1000
        expected_todo_key = "todo"
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(expected_status_msg, actual_response)
        self.assertEquals(expected_limit, response.json()["limit"])
        self.assertEquals(actual_time, expected_time)
        for i in range(len(response.json()["todos"])):
            actual_todo_dict = response.json()["todos"][i]
            self.assertIn(expected_todo_key, actual_todo_dict)
        for i in range(len(response.json()["todos"])):
            id_value = response.json()["todos"][i]["id"]
            self.assertTrue(isinstance(id_value, int))
