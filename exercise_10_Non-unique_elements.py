def checkio(data: list) -> list:
    dataUnique = []
    for item in data:
        if item not in dataUnique:
            dataUnique.append(item)

    return dataUnique


data = [1, 2, 3, 1, 3]

print(checkio(data))