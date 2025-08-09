def clean_text(text):
    return text.strip()


def count_words(text):
    return len(text.split())


def replace_word(text, old, new):
    return text.replace(old, new)


