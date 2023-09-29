import unittest

from api_requests.dummy_jason_requests_todo import DummyJsonRequestsToDo


class TestAddNewTodo(unittest.TestCase):

    def setUp(self):
        self.requests_handler = DummyJsonRequestsToDo()

    def test_add_new_todo_when_user_id_is_in_db(self):
        response = self.requests_handler.add_a_new_todo(todo="Use DummyJSON in the project", completed=False, userId=5)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_id = 151
        expected_user_id = 5
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(expected_response_status, response.reason)
        self.assertEquals(expected_id, response.json()["id"])
        self.assertEquals(expected_user_id, response.json()["userId"])

    def test_add_new_todo_when_user_id_is_not_in_db(self):
        response = self.requests_handler.add_a_new_todo(todo="Use DummyJSON in the project", completed=False, userId=155)
        expected_status_code = 404
        expected_response_status = "Not Found"
        expected_error = "User with id '155' not found"
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(expected_response_status, response.reason)
        self.assertEquals(expected_error, response.json()["message"])

    def test_add_new_todo_when_id_is_null(self):
        response = self.requests_handler.add_a_new_todo(todo="Use DummyJSON in the project", completed=False, userId=0)
        expected_status_code = 400
        expected_response_status = "Bad Request"
        expected_error = "User id is required"
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(expected_response_status, response.reason)
        self.assertEquals(expected_error, response.json()["message"])
