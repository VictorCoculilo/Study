def array_diff(a, b):
    new_list = []
    for number in a:
        if number not in b:
            new_list.append(number)
    return new_list