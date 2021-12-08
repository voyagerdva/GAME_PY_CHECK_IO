def frequency_sort(arr):
    elements = {}
    for item in arr:
        if not elements.get(item):
            elements[item] = 1
        else:
            elements[item] += 1

    result = []
    for k in elements.keys():
        for i in range(elements[k]):
            result.append(k)

    return result




arr = [4, 6, 2, 2, 2, 6, 4, 4, 4]

print(frequency_sort(arr))
