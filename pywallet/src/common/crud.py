from typing import Callable, Awaitable, TypeVar, ParamSpec
from functools import wraps

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.models import User, Wallet
from schemas.responses import UsersResponse, UserResponse, WalletsResponse, WalletResponse
from schemas.reqs import CreateUserRequest, CreateWalletRequest

P = ParamSpec("P")
T = TypeVar("T")

def transactional(func: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]:
    @wraps(func)
    async def wrapper(self: object, session: AsyncSession, *args: P.args, **kwargs: P.kwargs) -> T:
        try:
            result = await func(self, session, *args, **kwargs)
            await session.commit()
            return result
        except Exception as ex:
            await session.rollback()
            raise
    return wrapper

class UserController:
    @transactional
    async def get_all_users(self: object, session: AsyncSession) -> UsersResponse:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return [
            UserResponse(uuid=user.uid, username=user.username, password_hash=user.password_hash, wallets=[])
            for user in users
        ]

    @transactional
    async def create_user(self: object, session: AsyncSession, creds: CreateUserRequest) -> UserResponse:
        user = User(username=creds.username, password_hash=creds.password)
        session.add(user)
        await session.flush()
        return UserResponse(uuid=user.uid, username=user.username, password_hash=user.password_hash)

class WalletController:
    @transactional
    async def get_all_wallets(self: object, session: AsyncSession) -> WalletsResponse:
        result = await session.execute(select(Wallet))
        wallets = result.scalars().all()
        return [
            WalletResponse(uuid=w.uid, balance=w.balance, owner_uuid=w.owner_id)
            for w in wallets
        ]

    @transactional
    async def create_wallet(self: object, session: AsyncSession, creds: CreateWalletRequest) -> WalletResponse:
        wallet = Wallet(owner_id="asdasd")
        session.add(wallet)
        await session.flush()
        return WalletResponse(uuid=wallet.uid, balance=wallet.balance, owner_uuid=wallet.owner_id)

    @transactional
    async def get_wallet(self: object, session: AsyncSession, wallet_id: str = "") -> WalletResponse:
        result = await session.execute(select(Wallet).where(Wallet.uid == wallet_id))
        wallet = result.scalar_one_or_none()
        if wallet is None:
            return WalletsResponse()
        return WalletResponse(uuid=wallet.uid, balance=wallet.balance, owner_uuid=wallet.owner_id)


class DatabaseCrud(UserController, WalletController):
    def __init__(self) -> None:
        super().__init__()

