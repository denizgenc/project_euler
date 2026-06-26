#!/usr/bin/env python3
# In the 20x20 grid [in file p_0011.txt], four numbers along a diagonal line have been marked in red.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left,
# right, or diagonally) in the 20x20 grid?

# I want to make a windowing iterator for this

def window_vhd(data: list, width: int, height: int, stride: int):
    """
    Iterator that takes a 1D list of objects, and then yields lists of adjacent objects, of length
    stride, in the following order:
        - horizontally adjacent
        - vertically adjacent
        - diagonally top-left to bottom-right ( \\ )
        - diagonally bottom-left to top-right ( / )

    To determine which objects are adjacent, the iterator needs a width and a height. It then orders
    them into a width x height grid, row by row. E.g.
        window(['a', 'b', 'c', 'd'], 2, 2, 1)
    will assume the items are arranged as follows:
        'a' 'b'
        'c' 'd'

    Note to self: for all of the range calculations, I have to substitute stride with (stride - 1).
    I'm pretty sure that I was running into the fencepost problem but I'm too tired to puzzle out
    how exactly it was manifesting here
    """
    if stride > width:
        raise ValueError("Stride is greater than width")
    if stride > height:
        raise ValueError("Stride is greater than height")

    DATA_LENGTH = len(data)

    # yield horizontally adjacent objects
    for row in range(DATA_LENGTH // width):
        for i in range(width - (stride - 1)):
            offset = (row * width) + i
            yield data[offset : offset + stride]

    final_row = DATA_LENGTH % width # check for row at end that is shorter than the full width
    if final_row > 0 and stride < final_row:
        for i in range(DATA_LENGTH - final_row, DATA_LENGTH - (stride - 1)):
            yield data[i : i + stride]

    # yield vertically adjacent objects
    for i in range(DATA_LENGTH - (width * (stride - 1))):
        yield data[i : i + (width * stride) : width]

    # yield \ directional diagonally adjacent objects
    # TODO

    # yield / directional diagonally adjacent objects
    # TODO

if __name__ == "__main__":
    l = [i for i in range(1, 108)]
    for i in window_vhd(l, 10, 10, 5):
        print(i)
