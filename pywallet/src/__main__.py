from fastapi import FastAPI, APIRouter
from schemas import responses as res
import uvicorn
from handlers.v1 import router as v1_router
from common import database
import asyncio

app: FastAPI = FastAPI()
app.include_router(v1_router)

@app.get('/health')
async def health() -> res.AnyResponse[res.HealthResponse]:
    return res.HealthResponse().as_res()

if __name__ == '__main__':
    asyncio.run(database.init_db())
    uvicorn.run('__main__:app', host='0.0.0.0', port=8000, reload=True)

# Привет Марат!
