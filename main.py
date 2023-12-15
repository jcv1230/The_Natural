from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer
from config.database import Session, engine, Base
from models.product import Product as ProductModel, Category as CategoryModel
from fastapi.encoders import jsonable_encoder
from typing import Optional, List

API = FastAPI()

API.title = "THE NATURAL"    
API.version = '1.0.0'

Base.metadata.create_all(bind=engine)

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request): # Se debe llamar si o si __call__ para que funcione y a su vez darle como parametro Request(Objeto de la clase Request)
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=401, detail="Invalid user")
        
class User(BaseModel):
    email:str
    password:str 
    
class Product(BaseModel):
    id: int = Field(default=0, title = "ID del Producto")
    name: str = Field(default="----", min_length=2, max_length=50, title = "Nombre del Producto")
    description: str = Field(default="-----", min_length=10, max_length=300, title = "Descripcion del Producto")
    price: float = Field(default=0, ge=0, title = "Precio del Producto" )
    category: str = Field(default="----", min_length=4, max_length=15, title = "Categoria del Producto")

class Category(BaseModel):
    category: str = Field(default="----", min_length=4, max_length=15, title = "Categoria del Producto")
    sub_category: str = Field(default="----", min_length=4, max_length=15, title = "Sub Categoria del Producto")

# Ruta para el Home
@API.get("/", tags=['Home'])
def message():
    return HTMLResponse(content="<h1> Market Place THE NATURAL</h1>")

# Ruta para el Login
@API.post("/login", tags=['auth'], response_model=dict, status_code=200)
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = create_token(data=user.model_dump())
        return JSONResponse(content={"token": token}, status_code=200)
    else:
        return JSONResponse(content={"message": "Invalid crentials"}, status_code=401)
    
# Get para obtener todos los productos
@API.get("/Product", tags=['Products'], response_model=List[Product], status_code=200) 
def get_product() -> List[Product]:
    db = Session()
    result = db.query(ProductModel).all() # SELECT * FROM movies
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Get filtrando por categoria los productos
@API.get("/Product/{sub_category}", tags=['Products'], status_code=200, response_model=Product)
def get_product_by_sub_category(sub_category: str) -> Product:
    db = Session()
    result = db.query(ProductModel).filter(ProductModel.sub_category == sub_category ).first()
    if result:
        return JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    
# Get para obtener todos las categorias
@API.get("/Category", tags=['Category'], response_model=List[Category], status_code=200) 
def get_category() -> List[Category]:
    db = Session()
    result = db.query(CategoryModel).all() 
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Get filtrando subcategorias por categoria
@API.get("/Category/{sub_category}", tags=['Category'], status_code=200, response_model=Category)
def get_category_by_sub_category(sub_category: str) -> Category:
    db = Session()
    result = db.query(CategoryModel).filter(ProductModel.sub_category == sub_category ).first()
    if result:
        return JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    
# Post para crear un producto
@API.post("/Product", tags=['Products'], response_model=dict, status_code=201)
def create_product(product: Product) -> dict:
    db = Session()
    new_product = ProductModel(**product.model_dump())
    db.add(new_product)
    db.commit()
    return JSONResponse(content={"message": "Product created successfully"},
                        status_code=201)

# Post para crear una categoria
@API.post("/Category", tags=['Category'], response_model=dict, status_code=201)
def create_category(category: Category) -> dict:
    db = Session()
    new_category = CategoryModel(**category.model_dump())
    db.add(new_category)
    db.commit()
    return JSONResponse(content={"message": "Category created successfully"},
                        status_code=201)
    
# Put para actualizar un producto
@API.put("/Product/{id}", tags=['Products'], response_model=dict, status_code=200)
def update_product(id: int, product: Product) -> dict:
    db = Session()
    result = db.query(ProductModel).filter(ProductModel.id == id).first()
    if not result:
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    result.name = product.name
    result.description = product.description
    result.price = product.price
    result.category = product.category
    db.commit()
    return JSONResponse(content={"message": "Product updated successfully"}, status_code=200)

# Put para actualizar una categoria
@API.put("/Category/{sub_category}", tags=['Category'], response_model=dict, status_code=200)
def update_category(sub_category: str, category: Category) -> dict:
    db = Session()
    result = db.query(CategoryModel).filter(CategoryModel.sub_category == sub_category).first()
    if not result:
        return JSONResponse(content={"message": "Category not found"}, status_code=404)
    result.categories = category.category
    result.sub_category = category.sub_category
    db.commit()
    return JSONResponse(content={"message": "Category updated successfully"}, status_code=200)

# Delete para eliminar un producto
@API.delete("/Product/{id}", tags=['Products'], response_model=dict)
def delete_product(id: int) -> dict:
    db = Session()
    result = db.query(ProductModel).filter(ProductModel.id == id).first()
    if not result:
        return JSONResponse(content={"message": "Product not found"}, status_code=404)
    db.delete(result)
    db.commit()
    return JSONResponse(content={"message": "Product deleted successfully"})

# Delete para eliminar una categoria
@API.delete("/Category/{sub_category}", tags=['Category'], response_model=dict)
def delete_category(sub_category: str) -> dict:
    db = Session()
    result = db.query(CategoryModel).filter(CategoryModel.sub_category == sub_category).first()
    if not result:
        return JSONResponse(content={"message": "Category not found"}, status_code=404)
    db.delete(result)
    db.commit()
    return JSONResponse(content={"message": "Category deleted successfully"})



    


