from abc import ABC, abstractmethod
from game_config.ui_style import *
import threading, sys, time, random

class LoadEffect(ABC):
    def __init__(self, message="Loading"):
        self.message = message
        self.running = False
        self.load_thread = None
        self.stop_event = threading.Event()

    @abstractmethod
    def _animation(self):
        pass

    def start(self):
        self.running = True
        self.stop_event.clear()
        self.load_thread = threading.Thread(target=self._animation)
        self.load_thread.daemon = True
        self.load_thread.start()

    def stop(self):
        self.running = False
        self.stop_event.set()
        if self.load_thread and self.load_thread.is_alive():
            self.load_thread.join(timeout=2)
            sys.stdout.write("\r" + (" " * (len(self.message) + 30)) + "\r")
            sys.stdout.flush()

class ShowChar(LoadEffect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_dot = "."
        self.NUM_DOT = 3

    def _animation(self):
        def showLoading(i):
            lineNum_style.startStyle()
            sys.stdout.write("\r" + text[:i])
            hidden_style.startStyle()
            sys.stdout.write(text[i:] + "\r")
            reset()
            sys.stdout.flush()
            time.sleep(0.1)

        text = self.message + self.show_dot*self.NUM_DOT
        ln = len(self.message) + self.NUM_DOT
        while not self.stop_event.is_set():
            for i in range(ln + 1):
                showLoading(i)
            time.sleep(0.3)
            for i in range(ln, -1, -1):
                showLoading(i)
            time.sleep(0.3)

class ProcessProgress:
    def __init__(self, length):
        self.length = length
        self.progress = 0

    def __str__(self):
        sys.stdout.write("\r" + (" " * (self.length + 5)) + "\r")
        sys.stdout.flush()
        curr_progress = int((self.length * self.progress) / 100)
        bar = f"{f"{self.progress}%":^{self.length}}"
        for i in range(curr_progress):
            if bar[i] == " ":
                bar = bar[:i] + "=" + bar[i+1:]
        return f"[{bar}]"
        

    def update_progress(self, val):
        self.progress += val
        self.progress = min(self.progress, 100)

    def complete(self):
        return self.progress >= 100
        
if __name__ == "__main__":
    bar = ProcessProgress(30)
    while not bar.complete():
        bar.update_progress(random.randint(3, 10))
        time.sleep(random.uniform(0, 0.5))
        print(bar, end="", flush=True)
