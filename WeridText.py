import os
from numpy.random import shuffle
from string import whitespace, punctuation


def constants_index(text, separators_only = whitespace + punctuation):
    index = -1
    for space in separators_only:
        try:
            current = text[:index].index(space)
            if index == -1 or current < index:
                index = current
        except ValueError:
            continue
    return index

def shuffle_word(word):
    last = word[-1]
    first = word[0]
    mid_word = [i for i in word[1:-1]]
    while "".join(mid_word) == word[1:-1]:
        shuffle(mid_word)
    return first + "".join(mid_word) + last

def repair_word(word, words):
    for i, wd in enumerate(words):
        if word[0] != wd[0]:
            continue
        if len(word) != len(wd):
            continue
        if word[-1] != wd[-1]:
            continue
        for letter in word[1:-1]:
            if not letter in wd:
                continue
        words.remove(wd)
        return wd
    raise AttributeError("Have not found matching word. Bad template!")

def to_code(word):
    if len(word) < 4:
        return False
    word = word[1:-1]
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            return True
    return False

def encode(text, text_sep = '\n—weird—\n', separators_only = None):
    if separators_only is None:
        separators_only = whitespace + punctuation
    encod = text_sep
    words = []
    n = constants_index(text, separators_only=separators_only)
    while n != -1:
        word = text[:n]
        if not to_code(word):
            encod += text[:n + 1]
            text = text[n + 1:]
            n = constants_index(text, separators_only=separators_only)
            continue
        words.append(word)
        separator = text[n]
        encod += shuffle_word(word) + separator
        text = text[n + 1:]
        n = constants_index(text, separators_only=separators_only)
    word = text
    if to_code(word):
        words.append(word)
        word = shuffle_word(word)
    words.sort()
    encod += word + text_sep + " ".join(words)
    return encod

def decode(text, text_sep = '\n—weird—\n', separators_only = None):
    if text.count(text_sep) != 2:
        raise ValueError("Bad text to decode")

    if separators_only is None:
        separators_only = whitespace + punctuation

    text = text[len(text_sep):]
    m = text.index(text_sep)

    words = text[m + len(text_sep):]
    text = text[:m]
    words = words.strip().split(" ")
    
    decod = ""

    n = constants_index(text, separators_only=separators_only)
    while n != -1:
        word = text[:n]
        if not to_code(word):
            decod += text[:n + 1]
            text = text[n + 1:]
            n = constants_index(text, separators_only=separators_only)
            continue
        separator = text[n]
        decod += repair_word(word, words) + separator
        text = text[n + 1:]
        n = constants_index(text, separators_only=separators_only)
    word = text
    if to_code(word):
        words.append(word)
        word = repair_word(word, words)
    words.sort()
    decod += word
    return decod


if __name__ == "__main__":
    example_texts = "example_texts"
    text_file = "text_from_task.txt"
    with open(os.sep.join([example_texts, text_file]), "r") as f:
        text = f.read()

    print(encode(text))
    print("____________________________________")
    print(decode(encode(text)))
        



