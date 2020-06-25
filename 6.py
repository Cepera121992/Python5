# def study_hours():
#     all_hours = []
#

with open('text6.txt', 'r', encoding="utf-8") as my_text:
    all_text = my_text.readlines()
    my_lessons = []
    my_hours = []
    my_dict = {}
    for line in all_text:
        my_numbers = line.split()
        my_lessons.append(my_numbers[0])
        my_hours.append(my_numbers[1])
        my_hours.append(my_numbers[2])
        my_hours.append(my_numbers[3])
        # print(my_numbers)
    for i in :

    # my_sum_1 = my_hours[0] + my_hours[1] + my_hours[2]
    print(my_sum_1)

    # print(my_lessons)
    # print(my_hours)
