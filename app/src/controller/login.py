# import datetime
#
# from app.src.services.auth import encode_token, check_pwd
# from sqlalchemy.orm import Session
# from fastapi import HTTPException
# from app.src.schema.user import User, UserLogin
# from app.src.services.free_currency import SessionLocal
#
# db: Session = SessionLocal()
#
#
# async def upsert_token(username: str) -> str:
#     if user := db.query(User).filter(User.username == username).first():
#         user.token = await encode_token(user.username)
#         user.logged_at = datetime.datetime.now(datetime.UTC)
#         db.commit()
#         db.refresh(user)
#         db.close()
#         return user.token
#     db.close()
#     raise HTTPException(status_code=404, detail='User not found')
#
#
# async def match_user(username: str, password: str, login_ip: str, user_agent: str) -> bool:
#     if user := db.query(User).filter(User.username == username).first():
#         if match := await check_pwd(password, user.password):
#             login = UserLogin(username=user.username, logged_at=datetime.datetime.now(datetime.UTC),
#                               login_ip=login_ip, user_agent=user_agent)
#             db.add(login)
#             db.commit()
#             db.close()
#             return match
#     db.close()
#     return False
