import os
from random import shuffle
from string import whitespace, punctuation


def constants_index(text, separators_only = whitespace + punctuation):
    """Function return index first mark with separator_only in text.
    If in text is not mark with separator_only then return -1

    Args:
        text (string): text in wich search mark with separator_only
        separators_only (string, optional): string of marks. Defaults to whitespace+punctuation.

    Returns:
        int: index first mark with separator_only in text
    """    
    index = -1
    for space in separators_only:
        try:
            if index == -1:
                current = text.index(space)
            else:
                current = text[:index].index(space)
            if index == -1 or current < index:
                index = current
        except ValueError:
            continue
    return index

def shuffle_word(word):
    """Function shuffled word in this way, so first and last word are constant,
    but the remaining have to be other order. 


    Args:
        word (string): One word, this word has to be 
            longer than 3 marks and middle letters mustn't be identical.

    Returns:
        string: Word shufled in special way 
    """    
    last = word[-1]
    first = word[0]
    mid_word = [i for i in word[1:-1]]
    while "".join(mid_word) == word[1:-1]:
        shuffle(mid_word)
    return first + "".join(mid_word) + last

def repair_word(word, words):
    """ Function find and return word from words
    with the same pattern like word and remove this word from words.
    Two words have the same pattern if first and last letter are identically
    and the remaining are the same, but in other order.


    Args:
        word (string): Shuffled word to repair
        words (list of string): list of words

    Raises:
        AttributeError: When in words is not pattern to word.

    Returns:
        string: string from words with the same pattern like word.
    """    
    for wd in words:
        if word[0] != wd[0]:
            continue
        if len(word) != len(wd):
            continue
        if word[-1] != wd[-1]:
            continue
        if word == wd:
            continue
        ct = False
        for letter in word[1:-1]:
            if not letter in wd[1:-1]:
                ct = True
                break
        if ct:
            continue
        words.remove(wd)
        return wd
    raise AttributeError("Have not found matching word. Bad template!")

def to_code(word):
    """ Function check word is good to encode and decode.
        Property required in repair_word

    Args:
        word (string): word

    Returns:
        bool: True if word is good to encode and decode. False in opposed case
    """    
    if len(word) < 4:
        return False
    word = word[1:-1]
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            return True
    return False

def encode(text, text_sep = '\n-weird-\n', separators_only = None):
    """ Function encode text.
        Whitespace and punctuation is not encode.
        Word is not encode if is shorter than 4 or letters between first and last are identically.
        Encode is that first and last letter stay, and remaining letters are shuffled,
        that new word is other than old.
    Args:
        text (string): Some text.
        text_sep (str, optional): text at the beginning encoded word and between encoded text and encoded words. Defaults to '\n-weird-\n'.
        separators_only (string, optional): whitespace and punctuation if require . Defaults to string.whitespace + string.punctuation.
    Returns:
        string: encoded text
    """    
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

def decode(text, text_sep = '\n-weird-\n', separators_only = None):    
    """ Function encode text.
        Whitespace and punctuation is not encode.
        Word is not encode if is shorter than 4 or letters between first and last are identically.
        Encode is that first and last letter stay, and remaining letters are shuffled,
        that new word is other than old.
    Args:
        text (string): Some encoded text.
        text_sep (str, optional): text at the beginning encoded word and between encoded text and encoded words the same like in encode. Defaults to '\n—weird—\n'.
        separators_only (string, optional): whitespace and punctuation if require . Defaults to string.whitespace + string.punctuation.
    
    Raises:
        ValueError: if is bad pattern of text.
    
    Returns:
        string: decoded text
    """    
    if text.count(text_sep) < 2:
        raise ValueError("Bad text to decode")

    if separators_only is None:
        separators_only = whitespace + punctuation

    text = text[len(text_sep):]
    m = 0
    i = 0
    while text[m:].count(text_sep) > 0:
        i += 1
        m += text[m:].index(text_sep) + len(text_sep)
    m -= len(text_sep)

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
    text_file = "Test_from_task.txt"
    with open(os.sep.join([example_texts, text_file]), "r") as f:
        text = f.read()

    print(encode(text))
    print("____________________________________")
    print(decode(encode(text)))
    print("____________________________________")
    print(decode(encode(decode(encode(text)))))
        



