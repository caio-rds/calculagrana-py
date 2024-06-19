# import datetime
#
# from app.src.services.database import insert_one
#
#
# async def create_log(title: str, action: str, user_trigger: str) -> None:
#     await insert_one('logs', {
#         'title': title,
#         'action': action,
#         'user_trigger': user_trigger,
#         'date': datetime.datetime.now()
#     })
