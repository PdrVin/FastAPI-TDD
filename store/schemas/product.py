from typing import Optional
from pydantic import BaseModel, Field

from store.schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product Name")
    quantity: int = Field(..., description="Product Quantity")
    price: float = Field(..., description="Product Price")
    status: bool = Field(..., description="Product Status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn):
    ...


class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(None, description="Product Quantity")
    price: Optional[float] = Field(None, description="Product Price")
    status: Optional[bool] = Field(None, description="Product Status")


class ProductUpdateOut(ProductUpdate):
    ...
