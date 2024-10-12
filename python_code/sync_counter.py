#  Date & Time 14/04/2024, 22:35.
#  @author Mesfin Haftu

import time

def count1():
    print('One')
    time.sleep(1)
    print('Two')


def main():
    for _ in range(3):
        count1()

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"\'{__file__}\' \nexecuted in {elapsed:0.2f} seconds")

