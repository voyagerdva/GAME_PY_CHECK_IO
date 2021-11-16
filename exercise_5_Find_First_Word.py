import re

def first_word(expr: str):
    exprList = re.split(r'[., \,,]', expr)
    for word in exprList:
        if not word.isdigit() and word != "":
            return word

text = "123 ... sdf'ww.qwe XXX"

print(*text.split(), sep="\n")
print()
print("\n", first_word(text))

assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word("Hello.World") == "Hello"
print("Coding complete? Click 'Check' to earn cool rewards!")