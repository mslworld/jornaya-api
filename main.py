from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()

class PhoneNumber(BaseModel):
    number: str

# Fake bot handler
async def fake_bot_function(number):
    print(f"[BOT] Got number: {number}")
    # Future: Fill form here

@app.post("/submit-number")
async def submit_number(data: PhoneNumber):
    asyncio.create_task(fake_bot_function(data.number))
    return {"status": "received", "number": data.number}
