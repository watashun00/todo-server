#!/usr/bin/python
# coding: UTF-8

import requests

#正しい
def test_1():
    a = 1
    b = 2
    assert a != b



def test_get():
    response = requests.get("http://localhost:8080/api/v1/todo/1")

    text = '{"id": 1, "deadline": "2019-06-11T14:00:00+09:00", "title": "Report submission", "memo": ""}'

    assert text == response.text

def test_post():
    
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"deadline": "2019-12-22T14:00:00+09:00", "title": "Add data", "memo": ""}'
    response = requests.post('http://localhost:8080/api/v1/todo', headers=headers, data=data)
    
    text = '{"status": "success", "message": "registered", "id": 2}'
    
    assert text == response.text 

