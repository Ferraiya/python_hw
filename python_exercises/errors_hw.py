# 1. Напишіть програму, яка просить користувача ввести два числа і ділить перше на друге.
# Треба обробити ситуації:
# друге число — 0
# введено не число
# показати результат, якщо все ок
# і завжди писати в кінці: "Операція завершена"
from operator import truediv


class Divide:
    def __init__(self):
        pass

    @staticmethod
    def divide():
        first_digit = input("Введіть перше число: ")
        second_digit = input("Введіть друге число: ")
        result = int(first_digit) / int(second_digit)
        return result


division = Divide()
try:
    print(division.divide())
except ZeroDivisionError:
    print("Не можна ділити на нуль!!!")
except ValueError:
    print("Введено не число!!!")
finally:
    print("Операція завершена")


# 2. Тут може бути тіршки складно, але ми вже знаємо про наслідування і знаємо про перевизначення методу. Трішки не говорили ми детально про магічні методи, але проблем бути не має:
#  клас NotEnoughFundsError, який буде викликатись, якщо на рахунку недостатньо грошей.
# Функція withdraw(amount) має:
# приймати суму
# перевіряти, чи є стільки на балансі
# якщо ні — кидати NotEnoughFundsError
# обробити виключення в try/except
# Чому я заговорив про магічні методи? Бо одне з можливих рішень задачі - наслідування від Exception і реалізація свого методу str (перевизначення стандартного).

class NotEnoughFundsError(Exception):

    def __str__(self):
        return "Недостатньо грошів на рахунку"


class Withdraw:
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance

    def withdraw(self):
        if self.balance < self.amount:
            raise NotEnoughFundsError()
        print("Забирайте ваші гроші")


amount = int(input("Скільки хочете зняти? "))
balance = 2000
withdraw = Withdraw(amount, balance)

try:
    withdraw.withdraw()

except NotEnoughFundsError as nef:
    print(nef)


# 3. Створіть функцію check_password(password), яка:
# кидає ValueError, якщо пароль коротший за 8 символів
# кидає TypeError, якщо передане не str
# повертає "Пароль прийнято" якщо все добре
# finally — друкує "Перевірка завершена"

def check_password(password):
    if len(password) < 8:
        raise ValueError()
    elif not isinstance(password, str):
        raise TypeError("Password is not a string")
    print("Пароль прийнято")


try:
    check_password(input("Enter password: "))
except ValueError:
    print("пароль має бути більше 8 символів")
except TypeError:
    print("пароль не рядок")
finally:
    print("Операція завершена")
