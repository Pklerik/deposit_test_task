import pytest
from fastapi.testclient import TestClient
from typing import Optional, List, Dict
import datetime
from random import randint, choice
from tests import date_generator
import main

client = TestClient(main.deposit_app, "http://")

@pytest.fixture
def create_correct_request_body() -> List:
    correct_request_bodies = []
    correct_floats = [i / 10.0 for i in range(10, 81)]
    for i in range(5):
        correct_request_bodies.append(
            {
                "date": date_generator.random_date("01.01.2024", "01.01.2050"),
                "periods": randint(1, 60),
                "amount": randint(10_000, 3_000_000),
                "rate": choice(correct_floats)
                }
            )
    return correct_request_bodies

@pytest.fixture
def create_wrong_request_body() -> List:
    wrong_request_bodies = [
        {
            "error": "date must be in dd.mm.YYYY format",
            "request": {
                "date": "30.01.33",
                "periods": 2,
                "amount": 20000,
                "rate": 1
            }
        },
        {
            "error": "day is out of range for month",
            "request": {
                "date": "33.01.33",
                "periods": 2,
                "amount": 20000,
                "rate": 1
            }
        },
        {
            "error": "month must be in 1..12",
            "request": {
                "date": "31.13.33",
                "periods": 2,
                "amount": 20000,
                "rate": 1
            }
        },
        {
            "error": "periods must be between 1 and 60",
            "request": {
                "date": "31.01.2024",
                "periods": 0,
                "amount": 20000,
                "rate": 1
            }
        },
        {
            "error": "amount must be between 10 000 and 3 000 000",
            "request": {
                "date": "31.01.2024",
                "periods": 2,
                "amount": 5,
                "rate": 1
            }
        },
        {
            "error": "rate must be between 1.00 and 8.00",
            "request": {
                "date": "31.01.2024",
                "periods": 2,
                "amount": 20000,
                "rate": 0.5
            }
        }
    ]
    return wrong_request_bodies

def test_deposit(create_correct_request_body):
    for request_data in create_correct_request_body:
        response = client.post("/deposit", headers={ "Accept": "application/json", "Content-Type": "application/json" }, json=request_data)
        # assert response.text is dict
        assert response.status_code == 200
        
def test_deposit_erorrs(create_wrong_request_body):
    for request_error in create_wrong_request_body:
        response = client.post("/deposit", headers={ "Accept": "application/json", "Content-Type": "application/json" }, json=request_error.get("request"))
        assert response.status_code == 400
        assert response.json() == {'error': request_error.get("error")}
            
def test_data_validation():
    valid_requests_responses = [
        {
            "request" : {
                "date": "31.01.2021",
                "periods": 3,
                "amount": 10000,
                "rate": 6,
                },
            "response" : {
                "2021-01-31":10050.00,
                "2021-02-28":10100.25,
                "2021-03-31":10150.75,
                }
            },
        {
            "request" : {
                "date": "15.01.2021",
                "periods": 15,
                "amount": 1000000,
                "rate": 7
            },
            "response" : {
                "2021-01-15": 1005833.33,
                "2021-02-15": 1011700.69,
                "2021-03-15": 1017602.28,
                "2021-04-15": 1023538.30,
                "2021-05-15": 1029508.94,
                "2021-06-15": 1035514.40,
                "2021-07-15": 1041554.90,
                "2021-08-15": 1047630.64,
                "2021-09-15": 1053741.82,
                "2021-10-15": 1059888.65,
                "2021-11-15": 1066071.33,
                "2021-12-15": 1072290.08,
                "2022-01-15": 1078545.11,
                "2022-02-15": 1084836.62,
                "2022-03-15": 1091164.83
                },
            }
        ]
    
    for request_response in valid_requests_responses:
        request_data = request_response.get("request")
        response_data = request_response.get("response")
        response = client.post("/deposit", headers={ "Accept": "application/json", "Content-Type": "application/json" }, json=request_data)
        
        assert response.status_code == 200
        assert response.json() == response_data