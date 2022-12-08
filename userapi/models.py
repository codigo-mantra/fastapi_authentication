from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey
from settings.database import Base
from resources.schemas import Role

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    # is_active = Column(Boolean, default=True)
    hashed_password = Column(String)
    otp_secret = Column(String)
    disabled = Column(Boolean, default=False)
    user_role = Column(Enum(Role))