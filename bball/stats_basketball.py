
import numpy as np
from struct import unpack


def read_tuples(fn):

    # data consists of 16 integers (4 bytes each)
    fmt = "I" * 16
    NBYTES = 16 * 4

    with open(fn, 'rb') as f:
        flines = f.readlines()
    flines = b"".join(flines)

    # extract binary data (see README for format of resulting tuples)
    tups = [unpack(fmt, flines[i:i+NBYTES])
            for i in range(0, len(flines), NBYTES)]

    return tups


def get_positions(tups_):

    if isinstance(tups_, tuple):
        tups = list(tups_)
    elif isinstance(tups_, list):
        tups = tups_

    tups = list(zip(*tups))
    positions = list()
    for j in range(12):
        tmp = np.unravel_index(list(tups[j]), (400, 360), order='C')
        arr = np.concatenate((tmp[1][:,None], tmp[0][:,None]), axis=1)
        # convert to feet, and then center the players in the 'pixel'.
        # Note: the README was wrong about the footage of the grid.
        arr = arr.astype(float)
        arr *= 0.125
        arr += 0.0625
        positions.append(arr)

    return positions


def get_goals(tups_):

    if isinstance(tups_, tuple):
        tups = list(tups_)
    elif isinstance(tups_, list):
        tups = tups_

    goals = list(zip(*tups))[-1]

    g_y, g_x = np.unravel_index(goals, (10, 9), order='C')
    goals = np.concatenate((g_x[:,None], g_y[:,None]), axis=1)
    goals = (goals * 5.) + 2.5
    goals = np.ascontiguousarray(goals)

    return goals
