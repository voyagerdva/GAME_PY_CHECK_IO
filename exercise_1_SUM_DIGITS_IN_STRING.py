def sum_numbers(text: str) -> int:
    summ = 0
    for letter in text.split():
        if letter.isdigit():
            numList = map(lambda x: int(x), list(letter))
            summ += sum(numList)
    return summ

def sum_numbers2(text: str) -> int:
    summ = 0
    for letter in text.split():
        if letter.isdigit():
            summ += int(letter)
    return summ



str = "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
print(sum_numbers2(str))

print(list(str))

assert sum_numbers('hi') == 0
assert sum_numbers('who is 1st here') == 0
assert sum_numbers('my numbers is 2') == 2
assert sum_numbers2('This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year') == 3755
assert sum_numbers('5 plus 6 is') == 11
assert sum_numbers('') == 0
