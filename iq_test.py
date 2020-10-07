def iq_test(numbers):
    # your code here
    numbers = numbers.split()
    numbers = [int(num) for num in numbers]
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if len(even) > len(odd):
        for num in odd:
            if num % 2 == 1:
                return numbers.index(num) + 1
    else:
        for num in even:
            if num % 2 == 0:
                return numbers.index(num) + 1


print(iq_test("10 5 9 7 3"))
