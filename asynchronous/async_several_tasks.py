import asyncio
from random import randint


async def random_int_generator():
    current_int = randint(0, 9)
    print(current_int)
    yield current_int


event_loop = asyncio.get_event_loop()
task_list = [(random_int_generator()) for x in range(1, 10)]
for task in task_list:
    event_loop.create_task(task)
run = event_loop.run_forever()
pass
