from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from src.api import main_router
from src.security import security
from fastapi.middleware.cors import CORSMiddleware

from src.middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI(title="Olima QA")
app.include_router(main_router)
security.handle_errors(app)
app.mount("/", StaticFiles(directory="/Users/oleglokhtin/PycharmProjects/olima-qa-backend/src/static", html=True))

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:63342",
                                  "http://localhost:3000"
                                  ],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )

app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)

# python -m src.main