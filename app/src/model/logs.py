import datetime

from beanie import Document


class Log(Document):
    action: str
    message: str
    level: str
    user_trigger: str
    user_agent: str
    ip: str
    timestamp: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)

    class Settings:
        name = 'logs'