import fastapi
from fastapi import Request
from pydantic import BaseModel, Field

app = fastapi.FastAPI()


class Ja3Response(BaseModel):
    ja3_hash: str = Field(None, alias="hash")
    fingerprint: str = Field(None)
    ciphers: str = Field(None)
    curves: str = Field(None)
    protocol: str = Field(None)
    user_agent: str = Field(None)


@app.get('/', name="get ja3 info", response_model=Ja3Response)
async def ja3_info(request: Request):
    return {
        "hash": request.headers.get("x-ja3-hash"),
        "fingerprint": request.headers.get("x-ja3"),
        "ciphers": request.headers.get("x-ciphers"),
        "curves": request.headers.get("x-curves"),
        "protocol": request.headers.get("x-protocol"),
        "user_agent": request.headers.get("x-ua"),
    }
