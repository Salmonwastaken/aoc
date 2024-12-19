from datetime import datetime
import os

current_year = datetime.today().strftime("%Y")
current_day = datetime.today().strftime("%d")

prefix = f"day{str(current_day)}"

if prefix not in os.listdir(f"./aoc/{current_year}"):
    os.mkdir(f"./aoc/{current_year}/{prefix}")
    os.chdir(f"./aoc/{current_year}/{prefix}")
    with open(f"./day{str(current_day)}.py", "w") as file:
        file.write(r"""from aoc.helpers.lineReader import lineReader

content = lineReader()
""")

        open("./input.txt", "w")
