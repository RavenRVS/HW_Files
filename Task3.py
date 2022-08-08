
def sort_files(files):
    dict_str_in_files = {}
    for file in files:
        with open(file, encoding='utf-8') as f:
            text = f.readlines()
            size = len(text)
            dict_str_in_files[file] = size
    sort_files = sorted(dict_str_in_files.items(), key=lambda x: x[1])
    with open('Sum_file.txt', 'w', encoding='utf-8') as wr_string:
        for file in sort_files:
            name_file = file[0]
            size_file = file[1]
            wr_string.write(name_file + '\n')
            wr_string.write(str(size_file) + '\n')
            with open(name_file, encoding='utf-8') as file_for_write:
                for line in file_for_write:
                    wr_string.write(line + '\n')

my_files = sort_files(['1.txt','2.txt','3.txt']) #Указываем наименования файлов для сортировки

