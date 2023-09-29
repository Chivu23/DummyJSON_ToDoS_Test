import unittest

from api_requests.dummy_jason_requests_todo import DummyJsonRequestsToDo


class TestDeleteTodo(unittest.TestCase):

    def setUp(self):
        self.requests_handler = DummyJsonRequestsToDo()

    def test_delete_todo_when_id_is_in_db(self):
        response = self.requests_handler.delete_todo(todo_id=11)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_response_key_id = 11
        expected_response_key_is_deleted = True
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(expected_response_status, response.reason)
        self.assertEquals(expected_response_key_id, response.json()["id"])
        self.assertEquals(expected_response_key_is_deleted, response.json()["isDeleted"])
        self.assertTrue(response.json()["isDeleted"])

    def test_deleted_todo_when_id_in_not_in_db(self):
        response = self.requests_handler.delete_todo(todo_id=190)
        expected_status_code = 404
        expected_response_status = "Not Found"
        expected_msg_error = "Todo with id '190' not found"
        self.assertEquals(expected_status_code, response.status_code)
        self.assertEquals(expected_response_status, response.reason)
        self.assertEquals(expected_msg_error, response.json()["message"])
