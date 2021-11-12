# def checkioOdd(L):
#     summ = 0
#     mult = 0
#     for item in L:
#         if item % 2 == 0:
#             summ += item
#     if len(L) > 0:
#         mult = summ * L[-1]
#     return mult

def checkio(L):
    summ = 0
    mult = 0

    if L:
        for index in range(len(L)):
            if index % 2 == 0:
                summ = summ + L[index]

        mult = summ * L[-1]

    return mult

arr0 = []
arr1 = [2]
arr1_1 = [1,2]
arr10 = [1,2,3,4,5,6,7,8,9,10]

checkio1 = lambda array: sum(array[::2]) * sum(array[-1:])

print(checkio1(arr0))
print(checkio1(arr1))
print(checkio1(arr1_1))
print(checkio1(arr10))



# S = summ + item for item in L if item%2 == 0
