while True:
    try:
        file_name :str = input('Введите название нового файла: ')
        if len(file_name) < 3 or file_name.isalpha() == False:
            raise Exception
        with open(f'{file_name}.txt', 'w') as file:
            break
    except Exception:
        print('Некорректное название файла. Введите название заново.')
        continue