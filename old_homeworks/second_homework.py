# Написати функцію is_palindrome(text), яка приймає рядок text
# Перевіряє, чи є слово паліндромом
# Повертає True, якщо це паліндром, і False, якщо ні.
# Приклад: print(is_palindrome("hello"))  # False. (підказка, паліндром це слово, яке читається однаково, задом наперед і нормально)

def is_palindrome(text):
     bool_value = ""
     text = text.lower()
     if text == text[::-1]:
         bool_value = True
     else:
         bool_value = False

     return bool_value

print(is_palindrome(input("Введіть текст: ")))

# 2. Написати функцію repeat_text(text, times), яка повторює text times разів.
# print(repeat_text("Hi ", 3))   # "Hi Hi Hi "

def repeat_text(text, times):
     needed_text = text+" "
     return needed_text*times

print(repeat_text("aerawer", 3))

# 3. Написати функцію shorten_text(text, n), яка обрізає рядок до n символів і додає ..., якщо текст був довший.
# Якщо n більше довжини рядка — вивести якесь повідомлення про помилку.

def shorten_text(text, n):
    error_text = "Помилка! Рядок не можна скоротити"
    if len(text[0:n])<len(text):
        return text[0:n]+"..."
    elif len(text[0:n])==len(text):
        return text
    else:
        return error_text
print(shorten_text("textextext",3))

# 4. Написати функцію replace_word(text, old, new), яка замінює всі входження old на new
# Приклад print(replace_word("I love Python", "Python", "JavaScript")) # "I love JavaScript"

def replace_word(text, old, new):
    new_text = text.replace(old, new)
    return new_text

print(replace_word("I love Python", "Python", "JavaScript"))

# 5. Написати функцію count_words(text), яка рахує кількість слів у реченні. САМЕ СЛІВ! Приклад

def count_words(text):
    words_count = len(text.split(" "))
    return words_count

print(count_words("This is a very big and interesting text"))

# 6. Написати функцію swap_case(text), яка змінює великі літери на малі, а малі – на великі.
# Приклад: print(swap_case("Python"))       # "pYTHON"

def swap_case(text):
    swapped_text = text.swapcase()
    return swapped_text

print(swap_case(input("Введіть текст: ")))
