def checkio(expression):
    flag = 0
    for word in expression.split():
        if word.isdigit():
            flag = 0
        else:
            flag += 1
            if flag == 3:
                return True
    return False


if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

assert checkio("Hello World hello") == True, "Hello"
assert checkio("He is 123 man") == False, "123 man"
assert checkio("1 2 3 4") == False, "Digits"
assert checkio("bla bla bla bla") == True, "Bla Bla"
assert checkio("Hi") == False, "Hi"
print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# word = "qwe"
# print(word.isdigit())

