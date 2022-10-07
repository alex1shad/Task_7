with open('1.txt', 'rt', encoding='UTF-8') as file_1,\
        open('2.txt', 'rt', encoding='UTF-8') as file_2,\
        open('3.txt', 'rt', encoding='UTF-8') as file_3,\
        open('t.txt', 'a', encoding='UTF-8') as file_t:
    dict = {}
    dict['1.txt'] = [len(file_1.readlines()), file_1]
    dict['2.txt'] = [len(file_2.readlines()), file_2]
    dict['3.txt'] = [len(file_3.readlines()), file_3]
    file_1.seek(0)
    file_2.seek(0)
    file_3.seek(0)
    file_sorted = sorted(list(zip(dict.values(), dict.keys())))
    for el in file_sorted:
        file_t.write(f'{el[1]}\n{el[0][0]}\n{el[0][1].read().strip()}\n')