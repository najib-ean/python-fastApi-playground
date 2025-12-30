from fastapi import FastAPI
from models import Product

app = FastAPI()

products = [
    Product(id=1, name="Apple", description="Red fruit", price=10.5, quantity=5),
    Product(id=2, name="Banana", description="Yellow fruit", price=5.0, quantity=10)
]

@app.get("/")
def greeting():
    return "Welcome Najib"

@app.get("/products")
def getAllProducts():
    return products

@app.get("/products/{id}")
def getProductById(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}

@app.post("/products")
def createProduct(product: Product):
    products.append(product)
    return product

@app.put("/products/{id}")
def updateProduct(id: int, updatedProduct: Product):
    # --- can do this ---
    # for index, product in enumerate(products):
    #     if product.id == id:
    #         products[index] = updatedProduct
    #         return updatedProduct
    
    # --- or this ---
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = updatedProduct
            return "Product added successfully"
    return {"error": "Product not found"}

@app.delete("/products/{id}")
def deleteProduct(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            # products.remove(products[i]) # --> this can
            del products[i] # --> this also can
            return "Pruduct has been deleted successfully"
    return {"error": "Product not found"}