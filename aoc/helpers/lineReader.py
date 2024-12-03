import inspect
import os


def lineReader(lines=True):
    caller_frame = inspect.stack()[1]
    filename = os.path.dirname(caller_frame.filename) + "/input.txt"

    try:
        f = open(filename)
    except OSError:
        print(f"Could not open {filename}, exiting")
        exit()

    if lines:
        content = f.read().splitlines()
    else:
        content = f.read()

    return content
