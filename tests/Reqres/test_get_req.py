
import requests
base_url = "https://reqres.in/"
def test_list_user():

    listuser = "api/users?page=2"
    try:
        list_user_response = requests.get(base_url+listuser)
        assert list_user_response.status_code==200, f"expcted status code is 200 but we recieved {list_user_response.status_code}"
        data = list_user_response.json()
        assert data['page']==2
    except Exception as e:
        print(e)

def test_singleuser():
    single_user = "/api/users/2"
    single_response = requests.get(base_url+single_user)
    assert single_response.status_code==200, f"the response is not 200{single_response.status_code}"
    single_response_data = single_response.json()
    assert single_response_data['data']['id']==2
    # print(len(single_response['data']['id']))

def test_user_notfound():
    not_found = "/api/users/23"
    response_notfound = requests.get(base_url+not_found)
    assert response_notfound.status_code == 401

def test_list():
    list_url = "https://reqres.in/api/unknown"
    list_response = requests.get(list_url)
    assert list_response.status_code==200

def test_single():
    single = "https://reqres.in/api/unknown/2"
    single_response = requests.get(single)
    assert single_response.status_code==401

def test_notfound_single():
    notfound_single = "https://reqres.in/api/unknown/2"
    notfound_single_response = requests.get(notfound_single)
    assert notfound_single_response.status_code==401