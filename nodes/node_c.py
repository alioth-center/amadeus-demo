from amadeus.pipeline.api import Operator
from amadeus.log import logger
import asyncio


class NodeC(Operator):
    async def run(self, context, payload):
        logger.info("[app] NodeC is running")
        await asyncio.sleep(1)
        return True