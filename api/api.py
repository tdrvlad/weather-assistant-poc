from fastapi import FastAPI, HTTPException, Header
from typing import Optional
import uvicorn
from lm.assistant import Assistant
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class ChatInput(BaseModel):
    user_message: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    response_message: str
    session_id: str


app = FastAPI()
assistant = Assistant()


@app.post("/chat")
async def chat(chat_input: ChatInput):
    try:
        session_id, output = assistant(
            input_string=chat_input.user_message,
            session_id=chat_input.session_id
        )
        response = ChatResponse(
            response_message=output,
            session_id=session_id
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/status")
async def status():
    return {"status": 200}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
