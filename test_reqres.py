import json

import requests
from jsonschema import validate

from schemas import post_users

url = "https://reqres.in/api/users"

payload = {"name": "morpheus", "job": "leader"}

response = requests.request("POST", url, data=payload)

print(response.text)


# def test_schema_validate_from_file():
#     response = requests.post("https://reqres.in/api/users", data={"name": "morpheus", "job": "master"})
#     body = response.json()
#
#     assert response.status_code == 201
#     with open("post_users.json") as file:
#         validate(body, schema=json.loads(file.read()))


def test_name_job_200_variable():
    response = requests.get("https://reqres.in/api/users", data={"name": "morpheus", "job": "master"}, params = {"page": 2})
    body = response.json()
    print(body)

    assert response.status_code == 200
    validate(body, schema=post_users)

def test_first_last_name_201():

    response = requests.post(
        url="https://reqres.in/api/users",
        json={
                "first_name": "Anna",
                "last_name": "Frank"
            }
    )

    assert response.status_code == 201

def test_first_last_name_delete_204():

    response = requests.delete(
        url="https://reqres.in/api/users",
        json={
                "first_name": "Anna",
                "last_name": "Frank"
            }
    )

    assert response.status_code == 204

def test_first_last_name_put_404():

    response = requests.put(
        url="https://reqres.in/api/users",
        json={
                "first_name": "Anna",
                "last_name": "Frank"
            }
    )

    assert response.status_code == 404

def test_first_last_name_400():

    response = requests.post(
        url="https://reqres.in/api/users",
        json={
                "first_name": "Anna",
                "last_name1": "Frank"
            }
    )

    assert response.status_code == 201