from watchdog.events import FileSystemEventHandler


class FileString(FileSystemEventHandler):

    def __init__(self, file_path) -> None:
        self._file_path = file_path

    def on_any_event(self, event):
        not_need, name_file = str(event.src_path).split("\\")
        name_file, not_need = str(name_file).split(".")

        for char in name_file:
            if char in ['а', 'о', 'у', 'э', 'ы', 'я', 'ё', 'ю', 'е', 'и', 'a', 'e', 'i', 'o', 'u', 'y']:
                print(char.lower())
            else:
                print(char.upper())
        print('.....')