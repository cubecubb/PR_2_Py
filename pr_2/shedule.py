import time
import os
from watchdog.observers import Observer
from shedule_class import FileTracking

path :str = os.getcwd()
event_handler = FileTracking()
observer = Observer()
observer.schedule(event_handler, path, recursive = True)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()