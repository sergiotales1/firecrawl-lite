import psutil
import logging
import asyncio

async def monitor_resources(stop_event: asyncio.Event, interval: float = 0):
    while not stop_event.is_set():
        log_system_usage()
        await asyncio.sleep(interval)  # wait before logging again


logging.basicConfig(
    level=logging.INFO,  # or DEBUG for more verbosity
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger("crawler")


def log_system_usage():
    process = psutil.Process()
    cpu = psutil.cpu_percent(interval=None)
    mem = process.memory_info().rss / (1024 * 1024)  # MB
    logger.info(f"CPU usage: {cpu:.2f}% | RAM usage: {mem:.2f} MB")
