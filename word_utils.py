
def del_punctuation(sentence:str) -> str:
    import re
    return re.sub(r'[^\w\s]','',sentence)


def list_words(sentence:str) -> list:
    sentence = del_punctuation(sentence)
    return sentence.split()

def max_word(sentence:str) -> str:
    sentence = del_punctuation(sentence)
    sentence = list_words(sentence)
    return max(sentence, key=lambda x: len(x))

