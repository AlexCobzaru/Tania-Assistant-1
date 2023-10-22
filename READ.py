class read_files(object):
    def __init__(self, filename, element_number):
        self.filename = filename
        self.element_number = element_number-1

    def __str__(self):
        file = open(self.filename, encoding="utf-8")
        content = file.readlines()
        return str(content[self.element_number].split("\n")[0])

def language(text_file = "language 2.txt"):
    f = open(text_file, "rt", encoding="utf-8")
    text = f.read()
    return f"{text}"

def language_abreviation(text_file = "language 2.txt"):
    try:
        f = open(f"{language(text_file)}.txt", "rt", encoding="utf-8")
        text = f.readlines()
        return (text[0].split("\n")[0])
    except Exception as e:
        pass


def element(file, i):
    return read_files(file, i)

