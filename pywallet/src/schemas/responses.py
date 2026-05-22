from pydantic import BaseModel
from typing import Union, Dict, List, Optional

class AnyResponse[T](BaseModel):
    status_code: int = 200
    data: Optional[T] = None

    def __repr__(self: object) -> str:
        return f'status_code={self.status_code}, data={self.data}'


class WalletResponse(BaseModel):
    uuid: str = ""
    balance: int = 0
    wallet_name: str = "No name"
    owner_uuid: str = ""

    def as_res(self: object) -> AnyResponse[object]:
        return AnyResponse[WalletResponse](data=self)


type WalletsResponse = List[WalletResponse]


class HealthResponse(BaseModel):
    message: str = "Yeah, Im ok."
    
    def as_res(self: object) -> AnyResponse[object]:
        return AnyResponse[HealthResponse](data=self)

