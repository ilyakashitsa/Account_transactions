import json
from datetime import datetime


def read_operations_from_file(file_path):
    """
    Читает данные операций из файла JSON и возвращает список операций.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def format_card_number(card_number):
    """
    Форматирует номер карты, оставляя только первые 6 и последние 4 цифры.
    """
    return '{} **** **** {}'.format(card_number[:6], card_number[-4:])


def format_account_number(account_number):
    """
    Форматирует номер счета, оставляя только последние 4 цифры.
    """
    return '**{}'.format(account_number[-4:])


def format_operation_date(date):
    """
    Форматирует дату операции в требуемый формат (ДД.ММ.ГГГГ).
    """
    return datetime.fromisoformat(date).strftime('%d.%m.%Y')


def display_last_executed_operations(operations):
    """
    Выводит на экран информацию о последних пяти выполненных операциях.
    """
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda op: datetime.fromisoformat(op['date']), reverse=True)
    for op in sorted_operations[:5]:
        print('{} {}'.format(format_operation_date(op['date']), op['description']))
        print('{} -> {}'.format(format_card_number(op.get('from', 'Unknown')), format_account_number(op.get('to', 'Unknown'))))
        amount = op.get('operationAmount', {})
        print('{} {}'.format(amount.get('amount', 'Unknown'), amount.get('currency', 'Unknown')))


if __name__ == "__main__":
    file_path = 'operations.json'
    operations = read_operations_from_file(file_path)
    display_last_executed_operations(operations)
