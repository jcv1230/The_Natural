THE NATURAL API

Este proyecto es una API construida con FastAPI para un mercado llamado "THE NATURAL". La API permite la gestión de productos, categorías y proveedores.
Funcionalidades

  •	Autenticación de usuarios.
  •	CRUD (Crear, Leer, Actualizar, Eliminar) de productos, categorías y proveedores.
  •	Filtrado de productos por subcategoría, categorías por categoría principal y proveedores por ciudad.
  •	Endpoints

Endpoints

  •	/: Página de inicio.
  •	/login: Autenticación de usuarios.
  •	/Product: CRUD de productos.
  •	/Category: CRUD de categorías.
  •	/Supplier: CRUD de proveedores.
  
Modelos de datos

  •	User: Representa a un usuario con email y contraseña.
  •	Product: Representa a un producto con id, id del proveedor, nombre, descripción, precio y subcategoría.
  •	Category: Representa a una categoría con categoría principal y subcategoría.
  •	Supplier: Representa a un proveedor con id, nombre, dirección, teléfono, email y ciudad.
Autenticación

La autenticación se realiza mediante tokens JWT. Solo los usuarios con el email "admin@gmail.com" pueden autenticarse.

Base de datos

La API utiliza SQLAlchemy para interactuar con la base de datos. 
La base de datos utiliza como base las clases heredadas de BaseModel del modelo de datos, las tablas creadas con SQLAlchemy utilizan como columnas las claves del “objeto/diccionario” del Modelo de datos
