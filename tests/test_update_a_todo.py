import unittest


from api_requests.dummy_jason_requests_todo import DummyJsonRequestsToDo


class TestUpdateTodo(unittest.TestCase):

    def setUp(self):
        self.requests_handler = DummyJsonRequestsToDo()

    def test_update_todo_that_exist_in_db(self):
        response = self.requests_handler.update_todo(todo_id=1, completed=False)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_response_completed_key = False
        expected_response_key_id = 1
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(expected_response_status, response.reason)
        self.assertEquals(expected_response_completed_key, response.json()["completed"])
        self.assertEquals(expected_response_key_id, response.json()["id"])

    def test_update_todo_that_is_not_in_db(self):
        response = self.requests_handler.update_todo(todo_id=202, completed=False)
        expected_status_code = 404
        expected_response_status = "Not Found"
        expected_msg_error = "Todo with id '202' not found"
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(expected_response_status, response.reason)
        self.assertEquals(expected_msg_error, response.json()["message"])
