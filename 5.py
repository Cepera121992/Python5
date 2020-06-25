with open('text5.txt', 'x') as my_text:
    numbers = input('Введите любые числа через пробел: ').split()
    my_result = 0
    my_sum = 0
    for el in numbers:
        my_sum += int(el)
    my_result += my_sum
    print(my_result)
