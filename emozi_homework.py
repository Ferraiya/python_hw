# from emozi_functions import clean_text, count_words, replace_word
from emozi_functions import clean_text, count_words, replace_word
import emoji


def enter_text():
    text = input("Enter some text: ")
    return text


print(clean_text(enter_text()), emoji.emojize(":smiling_face_with_sunglasses:"))
print(count_words(enter_text()), emoji.emojize(":smiling_face_with_halo:"))
print(replace_word(enter_text(), input("Old text: "), input("New text: ")), emoji.emojize(":ZZZ:"))
