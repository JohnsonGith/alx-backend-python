#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.
"""

import asyncio
import random

async def wait_random(max_delay: float = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (float, optional): The maximum delay in seconds (default is 10).

    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
