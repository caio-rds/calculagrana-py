import datetime

from beanie import Document, Indexed


class Log(Document):
    action: str
    message: str
    level: str
    user_trigger: Indexed(str)
    user_agent: str
    timestamp: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)

    class Settings:
        name = 'logs'
