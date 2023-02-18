
def int_to_string(my_int: int) -> str:
    temp = str()
    div_10 = int(10)
    while my_int:
        temp += str(int(my_int % div_10))
        my_int = int(my_int / div_10)

    out = temp[::-1]
    return out