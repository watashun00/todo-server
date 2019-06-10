#!/usr/bin/python
# coding: UTF-8

import requests

#正しいテスト
def test_1():
    a = 1
    b = 2
    assert a != b

#3つデータをポスト
def test_post_01():
    
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"deadline": "2019-12-22T14:00:00+09:00", "title": "Add data1", "memo": ""}'
    response = requests.post('http://localhost:8080/api/v1/todo', headers=headers, data=data)
    
    text = '{"status": "success", "message": "registered", "id": 1}'
    
    assert text == response.text 

def test_post_02():
    
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"deadline": "2019-12-22T14:00:00+09:00", "title": "Add data2", "memo": ""}'
    response = requests.post('http://localhost:8080/api/v1/todo', headers=headers, data=data)
    
    text = '{"status": "success", "message": "registered", "id": 2}'
    
    assert text == response.text 

def test_post_03():
    
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"deadline": "2019-12-22T14:00:00+09:00", "title": "Add data3", "memo": ""}'
    response = requests.post('http://localhost:8080/api/v1/todo', headers=headers, data=data)
    
    text = '{"status": "success", "message": "registered", "id": 3}'
    
    assert text == response.text 

#間違ったデータをPOST
#deadlineなし
def test_post_04():
    
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"title": "Add data4", "memo": ""}'
    response = requests.post('http://localhost:8080/api/v1/todo', headers=headers, data=data)
    
    text = '{"status": "failure", "message": "no deadline"}'
    
    assert text == response.text 

#titleなし
def test_post_05():
    
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"deadline": "2019-12-22T14:00:00+09:00", "memo": ""}'
    response = requests.post('http://localhost:8080/api/v1/todo', headers=headers, data=data)
    
    text = '{"status": "failure", "message": "no title"}'
    
    assert text == response.text 

#memoなし
def test_post_06():
    
    headers = {
        'Content-Type': 'application/json',
    }
    data = '{"deadline": "2019-12-22T14:00:00+09:00", "title": "Add data4"}'
    response = requests.post('http://localhost:8080/api/v1/todo', headers=headers, data=data)
    
    text = '{"status": "failure", "message": "no memo"}'
    
    assert text == response.text 

#2つ取得
def test_get_01():
    response = requests.get("http://localhost:8080/api/v1/todo/1")

    text = '{"id": 1, "deadline": "2019-12-22T14:00:00+09:00", "title": "Add data1", "memo": ""}'

    assert text == response.text

def test_get_02():
    response = requests.get("http://localhost:8080/api/v1/todo/2")

    text = '{"id": 2, "deadline": "2019-12-22T14:00:00+09:00", "title": "Add data2", "memo": ""}'

    assert text == response.text

#全取得
def test_get_03():
    response = requests.get("http://localhost:8080/api/v1/todo")

    text = '{"events": [{"id": 1, "deadline": "2019-12-22T14:00:00+09:00", "title": "Add data1", "memo": ""}, {"id": 2, "deadline": "2019-12-22T14:00:00+09:00", "title": "Add data2", "memo": ""}, {"id": 3, "deadline": "2019-12-22T14:00:00+09:00", "title": "Add data3", "memo": ""}]}'

    assert text == response.text