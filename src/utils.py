def buff_number(number):
    result = str(number)
    if (number < 10):
        result = "00" + str(number)
    elif (number < 99):
        result = "0" + str(number)
    return result