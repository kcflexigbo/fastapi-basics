import enum
import uuid

from pydantic import BaseModel, Field
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, ARRAY, JSONB
from sqlalchemy import Text, Enum

Base = declarative_base()

class UserRoleEnum(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    username = Column(Text, unique = True, nullable=False)
    password = Column(Text, nullable=False)
    role = Column(Enum(UserRoleEnum), nullable=False)

    Books = relationship("Books", back_populates="User")


class Books(Base):
    __tablename__ = "Books"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    title = Column(Text, index=True, nullable=False)
    serial_number = Column(Text, unique=True, nullable=False, index=True)
    author = Column(Text, nullable=False)
    user_id = Column(PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=True)

    User = relationship("User", back_populates="Books")

