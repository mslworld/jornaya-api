# main.py

from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()

# Model for phone number
class PhoneNumber(BaseModel):
    number: str

# Placeholder for future bot function
async def fake_bot_function(number):
    print(f"[BOT] Received number: {number}")
    # Yahan actual bot logic aye ga

# API Endpoint
@app.post("/submit-number")
async def submit_number(data: PhoneNumber):
    asyncio.create_task(fake_bot_function(data.number))
    return {"status": "received", "number": data.number}
