def average(salaries):
    my_sum = sum(salaries)
    count = len(salaries)
    answer = my_sum / count
    return answer


with open('text3.txt', 'r') as my_text:
    all_text = my_text.readlines()
    surnames = []
    salaries = []
    for line in all_text:
        i = 0
        my_surnames = line.split()
        surnames.append(my_surnames[i])
        salaries.append(int(my_surnames[i + 1]))
        my_average = average(salaries)
    print(surnames)
    print('Средняя зарплата сотрудников:', (int(my_average)), 'рублей')
