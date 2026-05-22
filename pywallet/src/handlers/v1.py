from fastapi import APIRouter, Depends
from typing import Dict, List
from schemas.responses import *
from schemas.reqs import *
from common.crud import WalletController, UserController
from common.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router: APIRouter = APIRouter(prefix='/api/v1')
wallet_ctrl = WalletController()
user_ctrl = UserController()

@router.get('/wallets')
async def get_all_wallets(session: AsyncSession = Depends(get_session)) -> AnyResponse[WalletsResponse]:
    wallets = await wallet_ctrl.get_all_wallets(session)
    return AnyResponse[WalletsResponse](data=wallets)

@router.get('/wallets/{wallet_uuid}')
async def get_wallet_by_id(session: AsyncSession = Depends(get_session), wallet_uuid: str = "") -> AnyResponse[WalletResponse]:
    wallet = await wallet_ctrl.get_wallet(session, wallet_uuid)
    return AnyResponse[WalletResponse](data=wallet)

@router.post('/wallets/create')
async def create_wallet(session: AsyncSession = Depends(get_session), data: CreateWalletRequest = None) -> AnyResponse[WalletResponse]:
    wallet = await wallet_ctrl.create_wallet(session, data)
    return AnyResponse[WalletResponse](data=wallet)

@router.get('/users')
async def get_all_users(session: AsyncSession = Depends(get_session)) -> AnyResponse[UsersResponse]:
    users = await user_ctrl.get_all_users(session)
    return AnyResponse[UsersResponse](data=users)

@router.post('/users')
async def create_user(session: AsyncSession = Depends(get_session), creds: CreateUserRequest = None) -> AnyResponse[UserResponse]:
    user = await user_ctrl.create_user(session, creds)
    return AnyResponse[UserResponse](data=user)