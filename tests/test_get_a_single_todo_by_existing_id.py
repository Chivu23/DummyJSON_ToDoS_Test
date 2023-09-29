import unittest

from api_requests.dummy_jason_requests_todo import DummyJsonRequestsToDo


class TestGetSingleTodos(unittest.TestCase):

    def setUp(self):
        self.requests_handler = DummyJsonRequestsToDo()

    def test_get_a_single_todo_by_existing_id(self):
        """
        Testing first attribute has correct characteristics
        """
        todo_id = 1
        todo_todo = "Do something nice for someone I care about"
        todo_completed = True
        todo_userId = 26
        response = self.requests_handler.get_a_todo_by_id(id=todo_id)
        self.assertEquals(todo_id, response.json()["id"])
        self.assertEquals(todo_completed, response.json()["completed"])
        self.assertEquals(todo_userId, response.json()["userId"])
        self.assertEquals(todo_todo, response.json()["todo"])

    def test_get_a_single_todo_by_NOT_valid_id(self):
        """
        Testing status code is 404
        Testing we have correct sting in response
        """
        todo_id = 151
        response = self.requests_handler.get_a_todo_by_id(id=todo_id)
        expected_status_code = 404
        expected_error = f"Todo with id '{todo_id}' not found"
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(expected_error, response.json()["message"])

    def test_todo_by_user_id(self):
        """
        Testing is same user id
        """
        user_id = 5
        response = self.requests_handler.get_a_todo_by_user_id(user_id)
        self.assertEquals(user_id, response.json()["todos"][0]["userId"])
