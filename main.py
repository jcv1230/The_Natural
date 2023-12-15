from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

API = FastAPI()

API.title = "THE NATURAL"    
API.version = '1.0.0'

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

