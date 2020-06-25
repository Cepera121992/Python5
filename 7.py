def my_average(lines):
    my_sum = sum(lines)
    count = len(lines)
    answer = my_sum / count
    return answer


with open('text7.txt', 'r', encoding="utf-8") as my_text:
    all_text = my_text.readlines()
    my_list_1 = []
    my_list_2 = []
    my_dict = {}
    for line in all_text:
        my_lines = line.split()
        my_lines_1 = int(my_lines[2]) - int(my_lines[3])
        if my_lines_1 > 0:
            my_list_1.append(my_lines_1)
            my_dict[my_lines[0]] = my_lines_1
        else:
            my_list_2.append(my_lines)
            my_dict[my_lines[0]] = my_lines_1
    my_average_1 = {}
    my_average_1['average_profit'] = my_average(my_list_1)
    new_list = [my_dict, my_average_1]
    print(new_list)
    print('Фирма с убытком:', my_list_2)
