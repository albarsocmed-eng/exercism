def is_positive_int(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    return number

def steps(number):
    int_valid = is_positive_int(number)
    number_state = int_valid
    step_counter = 0
    while number_state != 1:
        if number_state % 2 == 0:
            x = number_state // 2
            number_state = x
            step_counter += 1
        elif number_state % 2 != 0:
            y = number_state * 3 + 1
            number_state = y
            step_counter += 1
    return step_counter
