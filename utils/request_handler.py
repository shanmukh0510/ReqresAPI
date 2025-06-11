import json

import requests
from utils.logger import setup_logger

logger = setup_logger()
class APIClient():
    def __init__(self,base_url):
        self.base_url = base_url
        self.headers={"Content-Type":"application/json"}

    def get(self,endpoint,**kwargs):
        url = self.base_url+endpoint
        logger.info(f"GET Request to: {url}")
        response = requests.get(url,headers=self.headers,**kwargs)
        logger.info(f"Response [{response.status_code}]: {response.text}")
        return response

    def post(self,endpoint,data,**kwargs):
        url=self.base_url+endpoint
        logger.info(f"POST Request to: {url} | Payload: {json or data}")
        response=requests.post(url,headers=self.headers,json=data)
        logger.info(f"Response [{response.status_code}]: {response.text}")
        return response

    def put(self,endpoint,data,**kwargs):
        url = self.base_url+endpoint
        logger.info(f"PUT Request to: {url} | Data: {data}")
        response = requests.put(url,headers=self.headers,json=data)
        logger.info(f"Response [{response.status_code}]: {response.text}")
        return response
    def delete(self,endpoint,**kwargs):
        url = self.base_url+endpoint
        logger.info(f"DELETE Request to: {url}")
        response = requests.delete(url,headers=self.headers)
        logger.info(f"Response [{response.status_code}]: {response.text}")
        return response
