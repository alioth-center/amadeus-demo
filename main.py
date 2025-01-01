from amadeus.pipeline.pipeline import PipelineLoader, Pipeline
from amadeus.config.read import global_config, read_global_config
from amadeus.log import logger, config_logger
import asyncio


if __name__ == "__main__":
    # 1. load global config and logger
    read_global_config("config/global.yaml")
    config_logger()  # default print to console
    # 2. load pipeline
    _loader = PipelineLoader()
    _loader.load()

    pipeline = _loader.build_pipeline("demo_ppl")

    # 3. set context and payload manually
    context = {}
    payload = {}

    pipeline.context = context
    pipeline.payload = payload

    async def run():
        # 4. run pipeline
        await pipeline.run()
    asyncio.run(run())