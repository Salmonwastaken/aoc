from typing import Union
import inspect
import os


def lineReader(lines: bool = True) -> Union[list[str], str]:
    caller_frame: list = inspect.stack()[1]
    filename = os.path.dirname(caller_frame.filename) + "/input.txt"

    try:
        f = open(filename)
    except OSError:
        print(f"Could not open {filename}, exiting")
        exit()

    if lines:
        return f.read().splitlines()
    else:
        return f.read()
