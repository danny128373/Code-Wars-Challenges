def reverse_integer(n):
    string_integer = str(n)
    list_of_digits = []

    for character in string_integer:
        list_of_digits.append(character)
    list_of_digits.reverse()

    return "".join(list_of_digits)


print(reverse_integer(123456789))
