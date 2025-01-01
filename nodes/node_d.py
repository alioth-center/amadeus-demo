from amadeus.pipeline.api import Operator
from amadeus.log import logger
import asyncio


class NodeD(Operator):
    async def run(self, context, payload):
        logger.info("[app] NodeD is running")
        await asyncio.sleep(1)
        return True