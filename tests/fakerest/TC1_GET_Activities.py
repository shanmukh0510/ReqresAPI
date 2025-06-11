import requests
import pytest
import json

def test_get_activities():
  url = "https://fakerestapi.azurewebsites.net//api/v1/Activities"

  headers = {"Content-Type":"application/json","Accept":"text/plain"}

  response = requests.get(url, headers=headers)

  assert response.status_code == 200
  data = response.json()
  print(f"\nResponse Json: {data}")