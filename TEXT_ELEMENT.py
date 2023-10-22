from READ import element
from READ import language

def TR(word_number, lg='language 2.txt'):
    return element(f"{language(lg)}.txt", 5 + word_number)
