import task
import pytest
from unittest.mock import patch, mock_open
import json

def test_task_1():
    result = task.task_1()
    assert result == 4880

def test_task_2_example_order():
    with patch("builtins.input", return_value="S4,P3,P7,X2,D4,C1,W2"):
        result = task.task_2()
        assert result == 48.49  # Total: 3.50 + 13.99 + 11.40 + 0.90 + 6.20 + 1.50 + 1.20

def test_task_2_different_order():
    with patch("builtins.input", return_value="P1,P2,X1"):
        result = task.task_2()
        assert result == 24.48  # Total: 8.99 + 13.99 + 1.50

def test_task_2_small_order():
    with patch("builtins.input", return_value="W1,W2"):
        result = task.task_2()
        assert result == 2.40  # Total: 1.20 + 1.20

def test_task_2_dessert_order():
    with patch("builtins.input", return_value="D1,D2,D3,D4"):
        result = task.task_2()
        assert result == 20.50  # Total: 4.40 + 5.30 + 4.60 + 6.20

def test_task_2_large_pasta_order():
    with patch("builtins.input", return_value="P10,P9,P8,P7"):
        result = task.task_2()
        assert result == 46.39  # Total: 11.50 + 10.99 + 12.50 + 11.40

def test_task_3_existing_user():
    # Mocking the content of contact.json
    mock_json_content = json.dumps({
        "Alice": {
            "phone": "123-456-7890",
            "email": "alice@example.com"
        },
        "Bob": {
            "phone": "987-654-3210",
            "email": "bob@example.com"
        },
        "Charlie": {
            "phone": "555-123-4567",
            "email": "charlie@example.com"
        }
    })

    # Patch the open function to simulate reading the JSON file
    with patch("builtins.open", mock_open(read_data=mock_json_content)):
        with patch("builtins.input", return_value="Charlie"):
            result = task.task_3()
            assert result == "Number: 555-123-4567, Email: charlie@example.com"

def test_task_3_non_existing_user():
    # Mocking the content of contact.json
    mock_json_content = json.dumps({
        "Alice": {
            "phone": "123-456-7890",
            "email": "alice@example.com"
        },
        "Bob": {
            "phone": "987-654-3210",
            "email": "bob@example.com"
        },
        "Charlie": {
            "phone": "555-123-4567",
            "email": "charlie@example.com"
        }
    })

    # Patch the open function to simulate reading the JSON file
    with patch("builtins.open", mock_open(read_data=mock_json_content)):
        with patch("builtins.input", return_value="David"):  # David does not exist
            result = task.task_3()
            assert result == "User not found."