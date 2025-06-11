import requests
def test_postresponse():
    url = "https://reqres.in/api/users"
    key = {"x-api-key": "reqres-free-v1"}
    payload = { "name": "morpheus",    "job": "leader"}
    response = requests.post(url, headers=payload,  data=key)
    # print(response.status_code)
    assert response.status_code == 201