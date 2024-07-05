from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel, Field

from store.schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product Name")
    quantity: int = Field(..., description="Product Quantity")
    price: float = Field(..., description="Product Price")
    status: bool = Field(..., description="Product Status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()


class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(None, description="Product Quantity")
    price: Optional[float] = Field(None, description="Product Price")
    status: Optional[bool] = Field(None, description="Product Status")


class ProductUpdateOut(ProductUpdate):
    ...
