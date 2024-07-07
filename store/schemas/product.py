from decimal import Decimal
from bson import Decimal128
from typing import Annotated, Optional
from pydantic import AfterValidator, BaseModel, Field

from store.schemas.base import BaseSchemaMixin, OutMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product Name")
    quantity: int = Field(..., description="Product Quantity")
    price: Decimal = Field(..., description="Product Price")
    status: bool = Field(..., description="Product Status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutMixin):
    ...


def convert_decimal_128(value):
    return Decimal128(str(value))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None, description="Product Quantity")
    price: Optional[Decimal_] = Field(None, description="Product Price")
    status: Optional[bool] = Field(None, description="Product Status")


class ProductUpdateOut(ProductUpdate, OutMixin):
    ...
