from amadeus.pipeline.api import Operator
from amadeus.log import logger
import asyncio


class NodeB(Operator):
    async def run(self, context, payload):
        logger.info("[app] NodeB is running")
        await asyncio.sleep(1)
        return True