# Створюємо калькулятор. Маємо чотири функції, дві я вам підкажу:

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Можна додавати тільки числа!")
    return a + b

def substract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Можна віднімати тільки числа!")
    return a - b

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Можна множити тільки числа!")
    return a * b

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Можна ділити тільки числа!")
    elif b == 0:
        raise ValueError("На нуль ділити не можна!")

    return a / b


#І завдання: Робимо тести. 4 позитивних (що все працює). І довільна кількість негативних, все придумаємо самі, які саме перевірки робити, які ні (це теж важливо), Використовуємо параметризацію при необхідності.

# 2. Завдання: є функція, яка читає файл data.txt і повертає кількість рядків у ньому.
# Щоб було ще швидше, я вам її даю:

def count_lines(file_path: str) -> int:
    with open(file_path, 'r', encoding='utf-8') as f:
        return len(f.readlines())

# Написати 2-3 тести на цю функцію. Тут є заковика, але підкажу, дуже зручно використовувати фікстуру для цього тесту.


