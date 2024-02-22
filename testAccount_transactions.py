import pytest
from utils import (
    read_operations_from_file,
    format_card_number,
    format_account_number,
    format_operation_date,
    display_last_executed_operations,
)


@pytest.fixture
def sample_operations():
    return read_operations_from_file('operations.json')

def test_read_operations_from_file():
    operations = read_operations_from_file('operations.json')
    assert isinstance(operations, list)
    assert len(operations) > 0


def test_format_card_number():
    card_number = '1234567890123456'
    formatted = format_card_number(card_number)
    assert formatted == '123456 **** **** 3456'

def test_format_account_number():
    account_number = '1234567890'
    formatted = format_account_number(account_number)
    assert formatted == '**7890'

def test_format_operation_date():
    date = '2024-02-21T12:00:00'
    formatted = format_operation_date(date)
    assert formatted == '21.02.2024'

def sample_operations():
    return [
        {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {
                "amount": "40701.91",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472"
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            }
        }
    ]


def test_display_last_executed_operations(capsys):
    display_last_executed_operations(sample_operations())
    captured = capsys.readouterr()
    output = captured.out.split('\n')

    assert len(output) == 7

    assert '08.12.2019 Открытие вклада' in output[0]
    assert 'Unknow **** **** nown -> **5907' in output[1]
    assert '41096.24 ' in output[2]
    assert '04.04.2018 Перевод организации' in output[3]
    assert 'Visa G **** **** 6353 -> **4472' in output[4]
    assert '40701.91' in output[5]
