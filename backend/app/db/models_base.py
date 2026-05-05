from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class CatalogBase(SQLModel):
    codigo: str = Field(primary_key=True, max_length=20)
    descripcion: str = Field(max_length=100)

class Rol(CatalogBase, table=True):
    __tablename__ = "roles"

class EstadoPedido(CatalogBase, table=True):
    __tablename__ = "estados_pedido"
    orden: int = Field(default=1)
    es_terminal: bool = Field(default=False)

class FormaPago(CatalogBase, table=True):
    __tablename__ = "formas_pago"
    habilitado: bool = Field(default=True)
