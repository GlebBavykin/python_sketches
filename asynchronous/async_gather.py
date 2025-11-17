import asyncio
from random import sample


async def get_some_values_from_io():
    return sample(range(0, 9), 5)


vals = []


async def fetcher():
    while True:
        io_vals = await get_some_values_from_io()

        for val in io_vals:
            vals.append(val)


async def monitor():
    while True:
        print(vals)
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(fetcher(), monitor())

asyncio.run(main())
