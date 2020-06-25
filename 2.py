with open('text2.txt', 'r') as my_text:
    all_lines = my_text.readlines()
    lines = 0
    words = 0
    for line in all_lines:
        wordslist = line.split()
        lines = lines + 1
        words = len(wordslist)
        print(f"Количество слов в {lines}-ой строке:", words)
    print('Количество строк:', lines)
