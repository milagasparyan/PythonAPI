from asyncio.windows_events import NULL
from importlib.metadata import files
from lib2to3.pgen2 import token
from urllib import response
import requests



URL = "https://gorest.co.in/public/v2/"

GET_API = "posts"

POST_API = "users"

GET_API1 = "users/1/"

POST_API2 = "users/1/todos"


def construct_url(common_url, api):
    return common_url + api

def test_get_status_code_equals_200():
    url = construct_url(URL, GET_API)
    response = requests.get(url)
    assert response.status_code == 200, print(
        "Got wrong status code, expected is: {}, actual is {}".format("200", response.status_code))


def test_post_status_code_201():
    url = construct_url(URL, POST_API)
    data = {
        "name":"Artur Matasyan", 
        "gender":"male",
        "email":"artur@mail.ru",
        "status":"active"
        }

    auth_token='ac47e01e02936cf24bd0bd97ffb92bbf47896f1f8178c05b57d1cb9e31dfa96a'
    hed = {'Authorization': 'Bearer ' + auth_token}


    response = requests.post(url, headers=hed, data=data )
    assert response.status_code == 201, print (
        "Got wrong status code, expected is: {}, actual is {}".format("201", response.status_code))


def test_post_status_code_401():
    url = construct_url(URL, POST_API)
    data = {
        "name":"Artur Matasyan", 
        "gender":"male",
        "email":"artur@mail.ru",
        "status":"active"
        }

    auth_token='mila'
    hed = {'Authorization': 'Bearer ' + auth_token}


    response = requests.post(url, headers=hed, data=data )
    assert response.status_code == 401, print (
        "Got wrong status code, expected is: {}, actual is {}".format("401", response.status_code))


def test_get_status_code_equals_404():
    url = construct_url(URL, GET_API1)
    response = requests.get(url)
    assert response.status_code == 404, print(
        "Got wrong status code, expected is: {}, actual is {}".format("404", response.status_code))

def test_post_status_code_422():
    url = construct_url(URL, POST_API2)
    data = { 
        "id":1864,
        "user_id":3776,
        "title":"Ipsam arx degenero vulgo cur.",
        "due_on":"2022-08-16T00:00:00.000+05:30",
    }
    auth_token='ac47e01e02936cf24bd0bd97ffb92bbf47896f1f8178c05b57d1cb9e31dfa96a'
    hed = {'Authorization': 'Bearer ' + auth_token}


    response = requests.post(url, headers=hed, data=data )
    assert response.status_code == 422, print (
        "Got wrong status code, expected is: {}, actual is {}".format("422", response.status_code))

def test_put_status_code_200():
    url = construct_url(URL, POST_API)
    data = {
        "name":"hhhhhhh", 
        "gender":"male",
        "email":"artur@mail.ru",
        "status":"active"
        }

    auth_token='ac47e01e02936cf24bd0bd97ffb92bbf47896f1f8178c05b57d1cb9e31dfa96a'
    hed = {'Authorization': 'Bearer ' + auth_token}


    response = requests.patch( url, headers=hed, data=data )
    assert response.status_code == 200, print (
        "Got wrong status code, expected is: {}, actual is {}".format("200", response.status_code))


def test_delete_status_code_200():
    url = construct_url(URL, GET_API1)
    data = {
        "name":"Artur Matasyan", 
        "gender":"male",
        "email":"artur@mail.ru",
        "status":"active"
        }

    auth_token='ac47e01e02936cf24bd0bd97ffb92bbf47896f1f8178c05b57d1cb9e31dfa96a'
    hed = {'Authorization': 'Bearer ' + auth_token}


    response = requests.delete(url, headers=hed, data=data )
    assert response.status_code == 200, print (
        "Got wrong status code, expected is: {}, actual is {}".format("200", response.status_code))        
