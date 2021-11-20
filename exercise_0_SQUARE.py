def square(length):
    i = 0
    side1 = str(i+1) * (length-1) + str(i+2)
    side24Line = "4" + " " * (length-2) + "2" + "\n"
    side24 = side24Line * (length-2)
    side3 = "4" + "3" * (length-1)

    result = f"{side1}\n{side24[:-1]}\n{side3}"
    return result

print(square(7))