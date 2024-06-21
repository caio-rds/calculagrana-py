from app.src.models.logs import Log
import logging


async def create_log(title: str, action: str, user_trigger: str, level: str = 'INFO') -> None:
    log = Log(
        action=action,
        message=title,
        level=level,
        user_trigger=user_trigger,
        user_agent='API')
    await log.insert()
    logging.log(
        level=getattr(logging, level),
        msg=f'{title} - {action} - {user_trigger}'
    )
