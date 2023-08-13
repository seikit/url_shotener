from fastapi import FastAPI
import uvicorn
from url_shortener.config.settings import settings
from url_shortener.routers.url import router

app = FastAPI(
    title=settings.app_name,
    summary=settings.summary,
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        app=settings.app,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        workers=settings.workers,
    )
