import requests
import jsonpath

def test_get_all():
    headers = {}
    response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1", headers=headers, params={})
    print(response.json())
    status = response.status_code
    assert status == 200


def test_create_item():
    headers = {}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": 'First title', "body": 'Some text some text', "userId": 1}
    )
    print(response.json())
    status = response.status_code
    assert status == 201
    new_post = response.json()
    assert new_post["title"] == "First title"
    assert new_post["body"] == "Some text some text"

def test_change_item():
    headers = {}
    response = requests.patch(
        "https://jsonplaceholder.typicode.com/posts/1",
        json={"title": "Changed Title"}
    )
    print(response.json())
    status = response.status_code
    assert status == 200

    updated_post = response.json()
    assert updated_post["title"] == "Changed Title"

def test_delete_item():
    headers = {}
    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1",
    )
    assert response.json() == {}
    status = response.status_code
    assert status == 200