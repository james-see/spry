import sys
import time

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def spinwhile():
    spinner = spinning_cursor()
    try:
        sys.stdout.write(spinner.next())
    except:
        sys.stdout.write(next(spinner)) # python 3
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')


