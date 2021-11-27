def bigger_price(N, table):
    resultValues = sorted([list(good.values())[1] for good in table], reverse=True)[:N]
    result = [item for item in table if list(item.values())[1] in resultValues]

    result.sort(key= lambda item: list(item.values())[1], reverse=True)

    return result
    # result = sorted(table, reverse=True, key=table)
    #
    # result = []
    # for item in table:
    #     # table.sort(reverse=True, key=item["price"])
    #     print(item["price"])
    #
    # # result = [table.sort(reverse=True, key=item["price"]) for item in table]
    # # result =
    # # pass
    # # return
    # # return table

table = [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]

N = 2

print(bigger_price(N, table))
