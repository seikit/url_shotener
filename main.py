from fastapi import FastAPI
from settings import settings
import uvicorn

app = FastAPI(
    title=settings.app_name,
    summary=settings.summary,
)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.host, port=settings.port)
