with open('text4.txt', 'r+') as my_text:
    all_text = my_text.readlines()
with open('text4_1.txt', 'x') as my_text_1:
    my_numbers = []
    for line in all_text:
        i = 0
        my_numbers_1 = line.split()
        my_numbers.append(my_numbers_1[i])
    my_numbers[0] = 'Один - 1'
    my_numbers[1] = 'Два - 2'
    my_numbers[2] = 'Три - 3'
    my_numbers[3] = 'Четыре - 4'
    print(my_numbers)

