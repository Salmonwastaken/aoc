from typing import Union
import inspect
import os


def lineReader(lines: bool = True) -> Union[list[str], str]:
    """
    Reads the content of an input file located in the same directory as the caller's script.

    Args:
        lines (bool): Whether to return the content as a list of lines (True) or as a single string (False).

    Returns:
        Union[list[str], str]: The content of the input file, either as a list of lines or a single string.

    Raises:
        SystemExit: If the file cannot be opened.
    """
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
