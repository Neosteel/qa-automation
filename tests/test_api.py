import requests
import pytest
import allure
@allure.feature("API Testing")
@allure.story("Get Post")
@allure.title("Verify GET request returns status 200 and correct data")
def test_get_post():

    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200
    data = response.json()
    print(data["id"])

    assert data["id"] == 1
    assert data["userId"] == 1

@allure.feature("API Testing")
@allure.story("Create Post")
@allure.title("Verify POST request creates new post with status 201")
def test_create_post():
    response = requests.post("https://jsonplaceholder.typicode.com/posts" , json = { 
        "title": "My Test Post",
        "body": "This is my test body",
        "userId": 1

    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "My Test Post"
    assert data["body"] == "This is my test body"
    assert data["userId"] == 1

@allure.feature("API Testing")
@allure.story("update post")
@allure.title("Verify PUT request updates post with status 200")
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

@allure.feature("API Testing")
@allure.story("delete post")
@allure.title("Verify DELETE request deletes post with status 200")
def test_delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200