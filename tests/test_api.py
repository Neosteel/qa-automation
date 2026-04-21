import requests
import pytest

def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200
    data = response.json()
    print(data["id"])

    assert data["id"] == 1
    assert data["userId"] == 1


def test_create_post():
    response = requests.post("https://jsonplaceholder.typicode.com/posts" , json = { 
        "title": "My Test Post",
        "body": "This is my test body",
        "userId": 1

    })
    assert response.status_code == 201
    data = response.json()
    data["title"] == "My Test Post"
    data["body"] == "This is my test body"
    data["userId"] == 1

def test_update_post():
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json={
            "title": "Updated Title",
            "body": "Updated body",
            "userId": 1
        }
    )
    assert response.status_code == 200
    
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["id"] == 1

def test_delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200