class FewChars(Exception):
    pass

while True:
    try:
        name_file :str = input()
        if len(name_file) < 3:
            raise FewChars
        if not name_file.isalpha():
            raise Exception
        for i in range(len(name_file)):
            if name_file[i].isdigit():
                raise Exception

    except FewChars:
        print('Недостаточно символов в имени файла')
        continue
    except Exception:
        print('Имя файла должно состоять из символов')
        continue
    else:
        with open(f"./File/{name_file}.txt", "a") as f:
            f.write('')