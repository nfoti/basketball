
import bball.stats_basketball
import matplotlib.pyplot as plt
import numpy as np

plt.ion()


if __name__ == "__main__":

    #fn = "/mnt/data/STATS_basketball_tracking/anon/train/poss-1_len-70.bin"
    import glob
    filenames = glob.glob("/mnt/data/STATS_basketball_tracking/anon/train/*.bin")

    for fn in filenames[8:9]:
        tups = bball.stats_basketball.read_tuples(fn)
        positions = bball.stats_basketball.get_positions(tups)
        goals = bball.stats_basketball.get_goals(tups)

        plt.figure()
        for i in range(1, 6):
            p_o = positions[i]
            p_d = positions[i+5]
            if i == 1:
                plt.plot(p_o[:,0], p_o[:,1], color='steelblue', linewidth=3)
            else:
                plt.plot(p_o[:,0], p_o[:,1], color='steelblue')
            plt.plot(p_d[:,0], p_d[:,1], color='darkred')

        ball = positions[0]
        plt.plot(ball[:,0], ball[:,1], color='goldenrod')

        plt.plot(goals[:,0], goals[:,1], '.', color='forestgreen')

        plt.pause(0.5)
        #plt.close()
