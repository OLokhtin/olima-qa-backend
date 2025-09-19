from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.api import main_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Olima QA")
app.include_router(main_router)
app.mount("/", StaticFiles(directory="/Users/oleglokhtin/PycharmProjects/olima-qa-backend/src/static", html=True))

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:63342",
                                  "http://localhost:3000"
                                  ],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )

if __name__ == "__main__":
     uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)

# python -m src.main