from src.services.base import ApiService

class UsersService(ApiService):
    def __init__(self):
        super().__init__()
        self.base_url = '/users'

    def get_users_list(self):
        return self.get('', )

    def get_user(self, user_id):
        return self.get(path=f'/{user_id}', headers = self.headers)

    def create_user(self, json):
        return self.post('', json=json)



