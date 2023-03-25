from enum import Enum
from pydantic import BaseModel


class BotStatus(str, Enum):
    """
    An enumeration of possible status values for the Discord bot.

    - SERVING: The bot is serving requests normally.
    - WARNING: The bot is experiencing issues that may affect its availability or performance.
    - CRITICAL: The bot is experiencing severe issues that are affecting its ability to serve requests.
    - OUTAGE: The bot is not available and cannot serve requests.
    """
    SERVING = "serving"
    WARNING = "warning"
    CRITICAL = "critical"
    OUTAGE = "outage"


class Bot(BaseModel):
    name: str
    status: BotStatus
    mission: str
