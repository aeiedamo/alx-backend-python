#!/usr/bin/env python3
"""
    You will spawn wait_random n times with the specified max_delay.
"""
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Waits for ran delay until max_delay, returns list of actual delays
    """
    spawn_list = []
    delay_list = []

    for i in range(n):
        delayed_task = asyncio.create_task(max_delay)
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)
    for spwn in spawn_list:
        await spwn

    return delay_list
