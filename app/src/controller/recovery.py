# import datetime
# import random
#
# from sqlalchemy.orm import Session
#
# from app.src.controller.user import read
# from app.src.schema.user import Recovery, User
# from app.src.services.auth import pwd_hash, check_pwd
# from app.src.services.free_currency import SessionLocal
# from app.src.model.user import RecoveryByPassword, RecoveryByCode
#
# # from app.src.services.logs import create_log
#
# db: Session = SessionLocal()
#
#
# async def user_request_code(username: str, ip: str) -> dict:
#     if user := await read(username=username):
#         if code_exists := db.query(Recovery).filter(Recovery.username == username).filter(Recovery.used == 0).first():
#             db.close()
#             return {
#                 "username": code_exists.username,
#                 "send_to": code_exists.send_to,
#                 "request_ip": code_exists.request_ip,
#                 "code": code_exists.code,
#                 "request_date": code_exists.request_date
#             }
#
#         new_code = Recovery(
#             code=await generate_code(),
#             username=user['username'],
#             way="email",
#             send_to=user['email'],
#             request_ip=ip,
#             request_date=datetime.datetime.now(datetime.UTC)
#         )
#         db.add(new_code)
#         db.commit()
#         db.refresh(new_code)
#         db.close()
#         return {
#             "username": new_code.username,
#             "send_to": new_code.send_to,
#             "request_ip": ip,
#             "code": new_code.code,
#             "request_date": new_code.request_date
#         }
#     db.close()
#     raise Exception('User not found')
#
#
# async def generate_code() -> str:
#     code = ''
#     for i in range(6):
#         code += str(random.randint(0, 9))
#     if db.query(Recovery).filter(Recovery.code == code).first():
#         db.close()
#         return await generate_code()
#     db.close()
#     return code
#
#
# async def recovery_by_code(recovery: RecoveryByCode) -> bool:
#     if code := db.query(Recovery).filter(
#             Recovery.username == recovery.username and Recovery.code == recovery.code).first():
#         if code.used == 0:
#             if user := db.query(User).filter(User.username == recovery.username).first():
#                 user.password = await pwd_hash(recovery.new_password)
#                 code.used = 1
#                 code.used_date = datetime.datetime.now(datetime.UTC)
#                 db.commit()
#                 db.close()
#                 return True
#         raise ValueError('Code already used')
#     db.close()
#     return False
#
#
# async def recovery_by_password(recovery: RecoveryByPassword) -> bool:
#     if user := db.query(User).filter(User.username == recovery.username).first():
#         if await check_pwd(recovery.password, user.password):
#             user.password = await pwd_hash(recovery.new_password)
#             db.commit()
#             db.close()
#             return True
#         raise ValueError('Password does not match')
#     db.close()
#     return False
