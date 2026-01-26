def is_armstrong_number(number):
    emp_list = []
    indvidual_digit = [int(i) for i in str(number)]
    power = len(str(number))
    
    for x in indvidual_digit:
        emp_list.append(x ** power)
        
    if sum(emp_list) == number:
        return True
    else:
        return False