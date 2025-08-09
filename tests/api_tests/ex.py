import requests
from src.services.users_service import UsersService


def test_get_all():
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.get("https://reqres.in/api/users", headers=headers, params={})
    print(response)
    status = response.status_code
    response_body = response.json()
    headers = response.headers
    response_str = response.text
    # my_cookies = response.cookies
    # my_token = response.json()['token']

    #assert response_body = response_json


#
def test_create_item():
    user_service = UsersService()
    all_users = user_service.get_users_list()
    my_user = {"name": "Apolli Green", "job": "Influencer"}
    response = UsersService().create_user(my_user)
    all_users_after = user_service.get_users_list()
    user_info = UsersService().get_user(response.json()['id'])

    # response = requests.post(
    #     "https://reqres.in/api/users",
    #     json=my_user,
    #     headers=headers
    # )


    assert response.status_code == 201
    assert user_info.json()['data']['first_name'] == my_user["name"]


#     headers.update({'Authorization': 'Bearer oafwfwgsd234153'})
#     second_response = requests.post('https://reqres.in/api/users', json={}, headers=headers)

def test_update_item():
    headers = {'x-api-key': 'reqres-free-v1'}
    my_user = {"name": "Apolli Green", "job": "Architect"}
    response = requests.put(
        "https://reqres.in/api/users/3",
        json=my_user,
        headers=headers
    )
    print(response)

def test_delete_item():
    headers = {'x-api-key': 'reqres-free-v1'}
    response = requests.delete(
          "https://reqres.in/api/users/13",
          headers=headers
        )
    print(response)


    # new_user_id = response.json()['id']
    # response = requests.get(f"https://reqres.in/api/users/{new_user_id}", headers=headers)
    # some = 1
    #
    # assert response.status_code == 201
    # assert response.json()['name'] == my_user['name']
    # assert response.json()['id'] == my_user['id']
    #
    # data = response.json()['data']
    # first_names = [names for names in data['first_name']]
    # response.get_values('$[data][*][first_name]')
    # assert my_user['name'] in first_names
