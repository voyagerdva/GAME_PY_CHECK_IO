def lessList(data, i):
    return data[:i] + data[i + 1:]


def checkio(data: list) -> list:
    i = 0

    if len(set(data)) == len(data):
        return []

    newData = []

    for item in data:
        if item in data[:i] + data[i + 1:]:
            i += 1
            newData.append(item)
            continue
        else:
            i += 1
            continue
    return newData


data = [10,20,30,10]

print(checkio(data))

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")