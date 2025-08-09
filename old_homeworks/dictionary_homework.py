# -Виведіть середню оцінку кожного студента
# -Знайдіть студента з найвищим середнім балом
# -Додайте нову оцінку Олегу

students = {
    "Anna": [90, 85, 78],
    "Ben": [76, 88, 90],
    "Oleg": [100, 90, 95]
}
new_dict = {}

for key in students:
    new_dict[key] = round(sum(students[key]) / len(students.get(key)), 1)

print(new_dict)
print(max(new_dict))

students["Oleg"].append(5)

print(students["Oleg"])

# 2. Напишіть просту "телефонну книгу". Як варіант - зробити 3-4 функції, які дозволяють додавати ім’я та номер телефону,
# шукати номер за ім'ям, видаляти номер, або його змінювати.

new_book = {}


def enter_names_and_phones():
    while True:
        input_name = input("Введіть ім'я: ", )
        input_phone = input("Введіть телефон: ", )

        new_book[input_name] = input_phone
        if input_name == "":
            break
    return "Наповнення довідника завершено."


def search_by_name():
    input_search = input("Шукати за іменем: ", )
    search = new_book.get(input_search, "Імя не знайдено")
    return search


def change_phone():
    input_change = input("Змінити телефон для імені: ", )
    new_phone = input("Новий телефон: ")
    new_book[input_change] = new_phone
    return "Телефон змінено успішно!"


def delete_item():
    input_delete = input("Видалити запис на імя: ", )
    new_book.pop(input_delete, "Запису не знайдено")
    return "Запис видалено!"


print(enter_names_and_phones(), search_by_name(), change_phone(), delete_item(), new_book)

# 3. pairs = [("apple", 2), ("banana", 3), ("orange", 1)]
#  Перетворіть список кортежів у словник. Той що вище.

pairs = [("apple", 2), ("banana", 3), ("orange", 1)]

print(dict(pairs))

# 4. data = {"a": 1, "b": 2, "c": 3}
# Своєрідний реверс. Поміняйте ключі і значення місцями. Має вийти такий словник
# {1: "a", 2: "b", 3: "c"}

data = {"a": 1, "b": 2, "c": 3}
data = {v: k for k, v in data.items()}

print(data)
