import asyncio
import time

# How to create tasks
async def my_task(secs):

    print(f'this task takes {secs} seconds to finish')
    time.sleep(secs)
    return 'task finished'


event_loop = asyncio.get_event_loop()
try:
    print('task created')
    task_obj = event_loop.create_task(my_task(5))
    event_loop.run_until_complete(task_obj)
finally:
    event_loop.close()
print(f'task result is {task_obj.result()}')