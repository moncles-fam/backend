from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware.timer_middleware import TimerMiddleware

app = FastAPI()

app.add_middleware(TimerMiddleware)

# CORS 미들웨어 추가 / test
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 오리진 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)