import requests


class DummyJsonRequestsToDo:

    _BASE_URL = "https://dummyjson.com/docs/todos"

    def get_all_todos(self, limit=None, skip=None):
        url = self._BASE_URL
        request_params = {}
        if limit is not None:
            request_params.update({"limit": limit})
        if skip is not None:
            request_params.update({"skip": skip})

        resp = requests.get(url=url, params=request_params)
        return resp

    def get_a_todo_by_id(self, id):
        url = f"{self._BASE_URL}/{id}"
        resp = requests.get(url=url)
        return resp

    def get_a_todo_by_user_id(self, userId):
        url = f"{self._BASE_URL}/user/{userId}"
        resp = requests.get(url=url)
        return resp

    def get_a_random_todo(self):
        url = f"{self._BASE_URL}/random"
        resp = requests.get(url=url)
        return resp

    def get_a_limit_and_skip_todos(self, limit, skip):
        url = f"{self._BASE_URL}/random"
        resp = requests.get(url=url)
        return resp

    def add_a_new_todo(self, todo, completed, userId):
        url = f"{self._BASE_URL}/add"
        request_body = {
            "todo": todo,
            "completed": completed,
            "userId": userId
        }
        resp = requests.post(url=url, json=request_body)
        return resp

    def update_todo(self, todo_id, completed):
        url = f"{self._BASE_URL}/{todo_id}"
        request_body = {
            "completed": completed
        }
        resp = requests.patch(url=url, json=request_body)
        return resp

    def delete_todo(self, todo_id):
        url = f"{self._BASE_URL}/{todo_id}"
        resp = requests.delete(url=url)
        return resp



# obj = DummyJsonRequestsToDo()
# response1 = obj.get_all_todos()
# print(response1.status_code)
# print(response1.json())