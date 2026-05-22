from sqlalchemy import Column, Integer, String, DateTime, BigInteger, Boolean
from sqlalchemy import func
import uuid
from common.database import Base


class User(Base):
    __tablename__ = 'users'

    uid = Column(String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    username = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Wallet(Base):
    __tablename__ = 'wallets'

    uid = Column(String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    balance = Column(BigInteger, nullable=True, default=0)
    owner_id = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

   
class Transaction(Base):
    __tablename__ = 'transactions'

    uid = Column(String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    wallet_id = Column(String, nullable=False)
    operation_type = Column(String, nullable=False, default="deposit")
    to_walled_id = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


