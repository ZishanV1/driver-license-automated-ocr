import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import subprocess
import sys

class Watcher:
    DIRECTORY_TO_WATCH = "/Users/zishan/Desktop/Excel_Test"  # Update to your directory

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        if event.is_directory:
            return None

        elif event.src_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Processing file: {event.src_path}")
            # Run the detect_test.py script and pass the newly created file as an argument
            subprocess.run([sys.executable, "/Users/zishan/Desktop/Excel_Test/detect_test.py", event.src_path])

if __name__ == '__main__':
    w = Watcher()
    w.run()
