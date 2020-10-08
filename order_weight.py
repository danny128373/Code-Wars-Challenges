def order_weight(strng):
    list_string = strng.split()
    list_of_tuples = []

    for num in list_string:
        sum = 0
        for i in range(len(num)):
            sum += int(num[i])
        list_of_tuples.append((sum, num))
    list_of_tuples = sorted(list_of_tuples, key=lambda x: x[0])
    new_list = []
    for tup in list_of_tuples:
        new_list.append(tup[1])
    print(" ".join(new_list))


print(order_weight("100 56 89 99 15 87 105"))
