import unittest

from api_requests.dummy_jason_requests_todo import DummyJsonRequestsToDo


class TestGetTodos(unittest.TestCase):

        def setUp(self):
            self.requests_handler = DummyJsonRequestsToDo()

        def test_all_todos(self):
            """
            Check :
            - status code 200
            - in response is 150 todos
            - status message is "OK"
            """

            response = self.requests_handler.get_all_todos()
            expected_status_code = 200
            expected_todos = 150
            expected_status_msg = "OK"
            self.assertEquals(expected_status_code, response.status_code)
            self.assertEquals(expected_todos, response.json()["total"])
            actual_status_msg = response.reason
            self.assertEquals(expected_status_msg, actual_status_msg)