from aoc.helpers.lineReader import lineReader
import re
import matplotlib.pyplot as plt


def findMiddle(i) -> int:
    return i // 2


def wrap(x, y, total_x, total_y):
    new_x = x % total_x
    new_y = y % total_y
    return new_x, new_y


if __name__ == "__main__":
    content = lineReader()

    cords_re = re.compile(r"-?\d+")

    total_x, total_y = 103, 101
    seconds = 0
    field = [[0 for _ in range(total_y)] for _ in range(total_x)]

    x_mid = findMiddle(total_x)
    y_mid = findMiddle(total_y)

    # Create a figure and axis for plotting
    fig, ax = plt.subplots()

    # Maximize the figure to fullscreen
    fig.set_size_inches(19.2, 10.8)  # Full HD aspect ratio (1920x1080)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Remove padding

    while True:
        positions = []
        for robot in content:
            (start_y, start_x, movement_y, movement_x) = [
                int(i) for i in re.findall(cords_re, robot)
            ]

            total_movement_x = movement_x * seconds
            total_movement_y = movement_y * seconds

            final_x = start_x + total_movement_x
            final_y = start_y + total_movement_y

            x, y = wrap(final_x, final_y, total_x, total_y)

            positions.append((x, y))

        for x, y in positions:
            field[x][y] = 1

        ax.clear()

        ax.imshow(field, cmap="viridis", interpolation="nearest", origin="upper")

        ax.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])

        # We save all the configurations and then just check what file has the lowest size
        # With the positions converging, the compression algorithm should have that create the smallest file :D
        # *it did*
        filename = f"images/grid_{seconds:03d}.png"
        plt.savefig(filename, bbox_inches="tight", pad_inches=0)

        for x, y in positions:
            field[x][y] = 0

        seconds += 1
