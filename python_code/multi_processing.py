#  Date & Time 14/04/2024, 21:56.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:55.
#  @author Mesfin Haftu

#  Date & Time 14/04/2024, 21:54.
#  @author Mesfin Haftu

#  Date & Time (\d+)", 1, "-")14/04/2024, 21:53.
#  @author Mesfin Haftu

from multiprocessing import Process, cpu_count
import time


# Multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
# multiprocessing = better for cpu bound tasks (heavy cpu usage)
# multithreading = better for io bound tasks (waiting around)
def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())
    a = Process(target=counter, args=(125_000_000,))
    b = Process(target=counter, args=(125_000_000,))
    c = Process(target=counter, args=(125_000_000,))
    d = Process(target=counter, args=(125_000_000,))
    e = Process(target=counter, args=(125_000_000,))
    f = Process(target=counter, args=(125_000_000,))
    g = Process(target=counter, args=(125_000_000,))
    h = Process(target=counter, args=(125_000_000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()


if __name__ == '__main__':
    t0 = time.perf_counter()
    main()
    print("Total time: ", (time.perf_counter() - t0), "Seconds.")
