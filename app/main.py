import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth.router import router as auth_router
from app.api.staffs.router import router as staff_router
from app.api.meat.router import router as meat_router
from app.api.products.router import router as products_router
from app.api.orders.router import router as orders_router
from app.api.needed_products.router import router as needed_products_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=auth_router, prefix="/auth", tags=["Auth"])
app.include_router(router=staff_router, prefix="/staff", tags=["Staff"])
app.include_router(router=orders_router, prefix="/order", tags=["Order"])
app.include_router(router=products_router, prefix="/product", tags=["Product"])
app.include_router(router=meat_router, prefix="/meat", tags=["Meat"])
app.include_router(
    router=needed_products_router, prefix="/auth", tags=["Needed products"]
)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True)
