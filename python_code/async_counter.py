#  Date & Time 14/04/2024, 22:07.
#  @author Mesfin Haftu
import asyncio
import time

async def count1():
    print('One1')
    await asyncio.sleep(1)
    print('Two1')

async def count2():
    print('One2')
    await asyncio.sleep(1)
    print('Two2')

async def count3():
    print('One3')
    await asyncio.sleep(1)
    print('Two3')

async def main():
    await asyncio.gather(count1(), count2(), count3())

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"\'{__file__}\' \nexecuted in {elapsed:0.2f} seconds")

# When each task reaches await asyncio.sleep(1),
# the function yells up to the event loop and gives control back to it,
# saying, “I’m going to be sleeping for 1 second.
# Go ahead and let something else meaningful be done in the meantime.”
