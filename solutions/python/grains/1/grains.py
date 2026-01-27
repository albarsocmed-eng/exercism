def square(number):
    d_value = number-1
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** d_value

def total():
    number_list = []
    for i in range(1, 65):
        doubling = square(i)
        number_list.append(doubling)
    return sum(number_list)
