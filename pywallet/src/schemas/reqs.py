from pydantic import BaseModel


class CreateWalletRequest(BaseModel):
    username: str = ""
    password: str = ""

type CreateUserRequest = CreateWalletRequest
