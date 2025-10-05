from fastapi import FastAPI, Depends, HTTPException,Header
from model import client,generation_config
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

API_KEY_CREDITS = {os.getenv("API_KEY") : 2}

def verify_api_key(api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(api_key,0)
    if credits <= 0:
        raise HTTPException(status_code=403, detail="Invalid or missing API key or limit exceeded of 2 requests")
    return api_key

@app.post("/generate")
def generate(prompt:str, api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[api_key] -= 1
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt, 
        config=generation_config
    )
    # for chunk in response:
    #     print(chunk.text)
    print(response.text)
    return {"response":response.text}


 
