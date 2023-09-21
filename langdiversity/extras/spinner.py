import itertools
import sys
import threading
import time
from contextlib import contextmanager

@contextmanager
def loading_spinner(label, current_step=None, total_steps=None):
    spinner_done = False

    def spinner_function():
        spinner = itertools.cycle(["-", "/", "|", "\\"])
        while not spinner_done:
            prefix = f"[{current_step}/{total_steps}] " if current_step is not None and total_steps is not None else ""
            sys.stdout.write(f'\r{prefix}{label} {next(spinner)}')
            sys.stdout.flush()
            time.sleep(0.1)
        print("\r", end="")
        print(f"{prefix}{label} ✓")

    spinner_thread = threading.Thread(target=spinner_function)
    spinner_thread.start()

    try:
        yield
    finally:
        spinner_done = True
        spinner_thread.join()


