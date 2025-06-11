import requests
head = {"x-api-key": "reqres-free-v1"}

def test_create():
    ulr_create = "https://reqres.in/api/users"
    payload = {
    "name": "morpheus",
    "job": "leader"}
    create_post = requests.post(ulr_create, json=payload, headers=head)
    print(create_post.status_code)

def test_put():
    url_put = "https://reqres.in/api/users/2"
    payload = {
    "name": "morpheus",
    "job": "zion resident"
}
    put_response = requests.put(url_put, json=payload, headers=head)
    assert put_response.status_code==200
    put_data = put_response.json()
    assert put_data['name']=="morpheus"

def test_patch():
    ult_patch = "https://reqres.in/api/users/2"
    payload = {
    "name": "morpheus",
    "job": "zion resident"
}
    patch_response = requests.patch(ult_patch, headers=head, json=payload)
    assert patch_response.status_code==200
    patch_data = patch_response.json()
    assert patch_data['name'] == "morpheus"

def test_delete():
    delete_url = "https://reqres.in/api/users/2"
    delete_response = requests.delete(delete_url)
    assert delete_response==204

def test_register():
    register_url = "https://reqres.in/api/register"
    payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
    register_response = requests.post(register_url, json=payload, headers=head)
    assert register_response.status_code==200
    register_data = register_response.json()
    assert register_data['id']==4

def test_badreq():
    bad_url = "https://reqres.in/api/register"
    payload = {
    "email": "sydney@fife"
}
    badurl_response = requests.post(bad_url, json=payload, headers=head)
    assert badurl_response.status_code==400
    bad_data = badurl_response.json()
    assert bad_data['error']=="Missing password"

def test_loginsucess():
    payload= {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
    login_sucessurl = "https://reqres.in/api/login"
    loginsuncess_response = requests.post(login_sucessurl, json=payload, headers=head)
    assert loginsuncess_response.status_code==200

    login_data = loginsuncess_response.json()
    assert login_data['token']=="QpwL5tke4Pnpja7X4"


def test_unsucess():
    url_unsucess = "https://reqres.in/api/login"
    payload = {
    "email": "peter@klaven"
}
    unscusee_response = requests.post(url_unsucess, json=payload, headers=head)
    assert unscusee_response.status_code == 400
    unsucess_data = unscusee_response.json()
    assert unsucess_data['error']=="Missing password"

def test_lasttest():
    last_url ="https://reqres.in/api/users?delay=3"
    last_response = requests.get(last_url, headers=head)
    assert last_response.status_code==200
