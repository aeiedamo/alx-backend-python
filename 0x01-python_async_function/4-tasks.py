#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n. The
code is nearly identical to wait_n except task_wait_random is being called.
"""
from typing import List
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    waits for ran delay until max_delay, returns list of actual delays.
    """
    spawn_list = []
    delay_list = []

    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)
    for spwn in spawn_list:
        await spwn

    return delay_list
