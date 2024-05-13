from datetime import datetime
import time
import cProfile, pstats, io
from pstats import SortKey


def add_operation(i):
    return 2*i + 2


def subtract_operation(i):
    num = 2*i - 2
    time.sleep(0.1)
    return num


class CustomTimer:

    def __init__(self):
        self.pr = cProfile.Profile()

    def start(self):
        # start the profiler
        self.pr.enable()

    def end(self):
        # stop the profiler
        self.pr.disable()

        # define the profiler results sorting criteria:
        # sort by the time spend in this and all sub functions from invocation till program exit
        sortby = SortKey.CUMULATIVE

        # create a statistics object from the profiler instance
        # using the sorting criteria
        ps = pstats.Stats(self.pr).sort_stats(sortby)

        # and print the 10 slowest operations to standard output stream
        ps.print_stats(10)


def main():
    timer = CustomTimer()

    timer.start()
    list_size = 100
    list_data = []
    for i in range(0, list_size):
        num = 0
        if (i % 2) == 0:
            num = add_operation(i)
        else:
            num = subtract_operation(i)

        list_data.append(num)

    timer.end()


if __name__ == "__main__":
    main()
