from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.user_router import router as user_router
from app.routers.product_router import router as product_router
from app.routers.auth_router import router as auth_router

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://fast-api-frontend-olive.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 TEMP FIX
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(user_router)
app.include_router(product_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Proffessional FastAPI backend running...."}