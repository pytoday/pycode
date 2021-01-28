
import asyncio

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(3)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(6)
    print('worker_2 done')

async def worker_3():
    print('worker_3 start')
    await asyncio.sleep(9)
    print('worker_3 done')

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    task3 = asyncio.create_task(worker_3())
    print('before await')
    await task1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')
    await task3
    print('awaited worker_3')

asyncio.run(main())

