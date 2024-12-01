import inspect
import os

def lineReader():
  caller_frame = inspect.stack()[1]
  filename = os.path.dirname(caller_frame.filename) + "/input.txt"

  try:
    f = open(filename)
  except OSError:
    print(f"Could not open {filename}, exiting")
    exit()

  content = f.read().splitlines()

  return content
