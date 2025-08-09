# Ctrl+Alt+L - форматування
# 1. Була схожа, але тут треба створити новий СПИСОК.
# numbers = [5, -3, 12, 0, -8, 7, -1, 4]
# Створи новий список, що містить тільки додатні числа
# Порахувати, скільки таких чисел

numbers = [5, -3, 12, 0, -8, 7, -1, 4]
posit_list = []
for i in numbers:
    if i > 0:
        posit_list.append(i)

print(len(posit_list))

# 2. ввести слово з клавіатури і перевірити чи воно є в списку. Якщо є - вивести індекс слова. Якщо немає - вивести текст, що такого слова немає у списку.

def find_word(word_input):

    words = ["apple", "banana", "cherry", "date", "kiwi"]

    if word_input in words:
        index = words.index(word_input)
        return index
    else:
        return "Слово не знайдене у списку"


print(find_word(input("введіть слово: ")))

# 3. Є два списки
# a = [1, 2, 3]
# b = [4, 5, 6]
# Об'єднайте їх у новий список c, але елементам цього нового списку буде значення помножене на 2. Тобто [2, 4, ....12]

a = [1, 2, 3]
b = [4, 5, 6]


def lists_merge(a, b):
    joined_list = a + b
    for i in range(len(joined_list)):
        joined_list[i] *= 2
    return joined_list


print(lists_merge(a, b))

# 4. phrases = ["  Hello ", "world ", " PYTHON ", " is ", " GREAT "]
# Тут треба Очисти всі рядки від пробілів та переведи до нижнього регістр.
# І вивести цей новий список, що вийшов.
#

phrases = ["  Hello ", "world ", " PYTHON ", " is ", " GREAT "]
lowerPhrases = [word.strip().lower() for word in phrases]

print(lowerPhrases)

# 5. Є список списків
# students = [
#     ["Anna", 90],
#     ["Ben", 75],
#     ["Oleg", 88]
# ]
# Вивести ім'я студента з найвищим балом.
# students = [["Anna", 90],["Ben", 75],["Oleg", 88]]
#

students = [["Anna", 90],["Ben", 95],["Oleg", 88]]
bestResult = max([students[0][1], students[1][1], students[2][1]])

if bestResult in students[0]:
    print (students[0][0])
elif bestResult in students[1]:
    print (students[1][0])
else: print (students[1][0])

# 6. Цю задачу спочату бажано точно не гуглити рішення. Спробувати самому
# values = [3, 5, 3, 7, 9, 5, 3, 9, 10]
# Створи список тільки з унікальних значень (без повторів)

values = [3, 5, 3, 7, 9, 5, 3, 9, 10]
unique_values = []
for i in values:
    if i not in unique_values:
        unique_values.append(i)

print(unique_values)