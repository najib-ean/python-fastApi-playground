from fastapi import FastAPI
from typing import Dict
from sqlalchemy import text
from core.config import settings
from database.db import get_db, init_db
from schemas.user import UserSchema
from router.user import router as user_router

app: FastAPI = FastAPI(title=settings.TITLE)
app.include_router(user_router, prefix="/api/v1")


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Hello World"}


@app.get("/health/db")
def health_check_db() -> Dict[str, str]:
    try:
        db = next(get_db())
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# @app.post("/register")
# def register_user(user: UserSchema):
#     print(user.email)
#     print(user.full_name)


# @app.get("/")
# def greeting():
#     return "Welcome Najib"


# @app.get("/products")
# def getAllProducts():
#     return products


# @app.get("/products/{id}")
# def getProductById(id: int):
#     for product in products:
#         if product.id == id:
#             return product
#     return {"error": "Product not found"}


# @app.post("/products")
# def createProduct(product: Product):
#     products.append(product)
#     return product


# @app.put("/products/{id}")
# def updateProduct(id: int, updatedProduct: Product):
#     # --- can do this ---
#     # for index, product in enumerate(products):
#     #     if product.id == id:
#     #         products[index] = updatedProduct
#     #         return updatedProduct

#     # --- or this ---
#     for i in range(len(products)):
#         if products[i].id == id:
#             products[i] = updatedProduct
#             return "Product added successfully"
#     return {"error": "Product not found"}


# @app.delete("/products/{id}")
# def deleteProduct(id: int):
#     for i in range(len(products)):
#         if products[i].id == id:
#             # products.remove(products[i]) # --> this can
#             del products[i]  # --> this also can
#             return "Pruduct has been deleted successfully"
#     return {"error": "Product not found"}
