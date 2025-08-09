# СТворіть клас Person з полями name, age, email. У ньому також створіть метод show_info() для виводу всіх даних
# Далі створіть клас Employee, який наслідує Person. У ньому створіть атрибути position і salary. І далі основне:
# Ваш метод show_info() - має виводити всю інформацію про працівника. (це можна зробити перевизначенням методу, або можете придумати щось своє))

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def show_info(self):
        print(f"Ім'я: {self.name} Вік: {self.age} Пошта: {self.email}")


class Employee(Person):
    def __init__(self, name, age, email, position, salary):
        super().__init__(name, age, email)
        self.position = position
        self.salary = salary

    def show_info(self):
        print(
            f"Ім'я: {self.name} Вік: {self.age} Пошта: {self.email}, Позиція: {self.position}, Заробітна плата: {self.salary}")


employee = Employee("Микола", 24, "mik@gmail.com", "QA", "1000$")
employee.show_info()


# Створіть клас PasswordUtils, який:
# Має атрибут об'єкта password (через def init).
# має метод change_password(new_password) — який змінює пароль.
# Має метод, задача якого перевірити чи є пароль надійним.
# На вхід подається люба строка, на виході True або False в залежності від того, чи ця строка пароль взагалі,
# і що він найдіний. Надійним пароль будемо вважати, якщо він довший 8 символів,
# якщо у ньому є хоч 1 цифра і якщо у ньому є хоч 1 велика літера.

class PasswordUtils:
    def __init__(self, password):
        self.password = password

    def change_password(self, new_password):
        self.password = new_password

    @staticmethod
    def is_strong_password(password):
        has_digit = any(char.isdigit() for char in password)
        has_upper = any(char.isupper() for char in password)
        if len(password) > 8 and has_digit and has_upper:
            return True
        return False

password_input = input("Введіть новий пароль: ")

print(PasswordUtils.is_strong_password(password_input))


# Створіть класс Book з атрибутами.
# Вам треба створити метод, який створить об'єкт классу Book з рядка такого формату.
# "The Hobbit|Tolkien|1937" і поверне це об'єкт у return

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)

    @classmethod
    def from_string(cls, book_info):
        title, author, year = book_info.split('|')
        return cls(title, author, year)


my_book = Book.from_string("The Hobbit|Tolkien|1937")
