from fastapi import FastAPI
from ua_parser import user_agent_parser

app = FastAPI(
    title="UA Parser API",
    description="Simple User Agent Parser API",
    version="0.1",
)

@app.get("/detect")
async def all(user_agent: str):
    # ua_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36'
    response = user_agent_parser.Parse(user_agent)
    return response
