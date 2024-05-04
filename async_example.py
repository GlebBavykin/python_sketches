import asyncio
from time import perf_counter
import logging
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters={
        'f': {'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
    },
    handlers={
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.INFO}
    },
    root={
        'handlers': ['h'],
        'level': logging.INFO,
    },
)

dictConfig(logging_config)

logger = logging.getLogger()
logger.info('often makes a very good meal of %s', 'visiting tourists')


async def count():
    logger.info(msg="One")
    await asyncio.sleep(1)
    logger.info(msg="Two")


async def tasks():
    await asyncio.gather(count(), count(), count(), count())


def main():
    s = perf_counter()
    asyncio.run(tasks())
    elapsed = perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


if __name__ == "__main__":
    main()

