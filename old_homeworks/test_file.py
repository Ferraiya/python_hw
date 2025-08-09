# 0. Виберіть собі довільне число від 50 до 250. Це ваше число секунд. Виведіть мені у консоль скільки це хвилин і секунд у форматі:
# "Число n - це m хвилин f секунд" (звісно підставити значення, які у вас вийшли)

sec = 70
ending = ""
ending1 = ""
hvylyna = sec // 60
zalyshok = sec % 60
hv = str(hvylyna)
value1 = hv[-1:]  #остання цифра хвилин

hv2 = str(zalyshok)
sec4 = hv2[-1:]  #остання цифра секунд

if int(value1) == 1:
    ending = "a"

elif int(value1) in range(2,5):
    ending = "и"
else:
    ending = ""

if zalyshok <=9:
    if int(sec4) == 1:
        ending1 = "a"
    elif int(sec4) in range(2, 5):
        ending1 = "и"
    else:
        ending1 = ""
else:
    sec3 = hv2[-2]  # передостання цифра секунд
    if int(sec3) == 1:
       ending1 = ""
    else:
        if int(sec4) == 1:
           ending1 = "a"
        elif int(sec4) in range(2,5):
           ending1 = "и"
        else:
            ending1 = ""


print("Число " + str(sec) + " - це "+ hv +" хвилин" + ending + " " + hv2 + " секунд" + ending1)

# 1. Дано список: numbers = [-5, 3, -1, 7, -2, 10]
# Виведіть тільки додатні числа.

mass = [-5, 3, -1, 7, -2, 10]
for i in mass:
    if i>0:
        print(i)

# 2. Є такий список чисел numbers = [3, 10, 7, 8, 15, 22, 31]
# Напишіть код, який їх перебере і виведе чи воно парне чи воно не парне. У такому форматі.
# "3 - непарне число". Так, можна прямо кирилицею.  (підказка - цикл for, і ділення без остачі на 2)

mass = [3, 10, 7, 8, 15, 22, 31]
for i in mass:
    if i%2 != 0:
        print(str(i) + " - непарне число")

# 3. Є рядок text = "Python is awesome" порахуйте скільки у ньому голосних і виведіть це у консоль:
# "Кількість голосних: тут ваша відповідь". (підказка, щоб перевірити чи міститься ваше значення у іншому є оператор "in", можна гуглити).

text = "Python is awesome"
newMass = []
wovels = ["a","e","i","o","u","y"]
for i in text:
    if i in wovels:
        newMass.append(i)
length = len(newMass)
print("Кількість голосних: "+ str(length))