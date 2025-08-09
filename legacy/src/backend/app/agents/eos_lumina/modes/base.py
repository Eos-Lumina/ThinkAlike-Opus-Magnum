import logging

class ModeModule:
    """
    Base class for all Eos Lumina modes.
    """
    def __init__(self, core: 'EosCore'):
        self.core = core
        self.logger = logging.getLogger(self.__class__.__name__)

    async def enter(self, context):
        self.logger.info(f"Entering {self.__class__.__name__}")
        return context

    async def handle_input(self, context):
        self.logger.warning(f"No handler implemented for {self.__class__.__name__}")
        return context

    async def exit(self, context):
        self.logger.info(f"Exiting {self.__class__.__name__}")
        return context
