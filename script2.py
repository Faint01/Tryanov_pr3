import time
from string_class import FileString
from watchdog.observers import Observer

path_to_file = r"File"
event_handler = FileString(path_to_file)
observer = Observer()
observer.schedule(event_handler, path=path_to_file, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
