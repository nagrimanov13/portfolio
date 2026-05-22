from fastapi import APIRouter
from typing import Dict, List
from schemas.responses import *
from schemas.reqs import *

router: APIRouter = APIRouter(prefix='/v1')

@router.get('/wallets')
async def get_all_wallets() -> AnyResponse[WalletsResponse]:
    return AnyResponse[WalletsResponse]()

@router.get('/wallets/{wallet_uuid}')
async def get_wallet_by_id(wallet_uuid: str = "") -> AnyResponse[WalletResponse]:
    return WalletResponse().as_res()

@router.post('/wallets/create')
async def create_wallet(data: CreateWalletRequest) -> AnyResponse[WalletResponse]:
    return WalletResponse().as_res()

