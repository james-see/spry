import sys
import time

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def spinwhile():
    spinner = spinning_cursor()
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')


