def count_digits(text):
    count = 0
    for letter in list(text):
        if letter.isdigit():
            count += 1
    return count

text = "lkj3 3 lkj3"
print(count_digits(text))
