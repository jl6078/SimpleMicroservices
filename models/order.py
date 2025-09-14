from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import date, datetime
from .person import PersonBase


class OrderBase(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Persistent Address ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )

    customer: PersonBase = Field(
        None,
        description="Customer",
        json_schema_extra={ 
            "example": [
                {
                    "uni": "abc1234",
                    "first_name": "Ada",
                    "last_name": "Lovelace",
                    "email": "ada@example.com",
                    "phone": "+1-212-555-0199",
                    "birth_date": "1815-12-10",
                    "addresses": [
                        {
                            "id": "550e8400-e29b-41d4-a716-446655440000",
                            "street": "123 Main St",
                            "city": "London",
                            "state": None,
                            "postal_code": "SW1A 1AA",
                            "country": "UK",
                        }
                    ],
                }
            ]
        },
    )
    item: str = Field(
        ...,
        description="Item being ordered.",
        json_schema_extra={"example": "Laptop"},
    )
    quantity: int = Field(
        ...,
        description="Quantity of the item ordered.",
        json_schema_extra={"example": 2},
    )
    price_per_item: float = Field(
        ...,
        description="Price per individual item.",
        json_schema_extra={"example": 999.99},
    )
    order_date: date = Field(
        ...,
        description="Date when the order was placed (YYYY-MM-DD).",
        json_schema_extra={"example": "2023-10-05"},
    )


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "customer": {
                        "uni": "abc1234",
                        "first_name": "Ada",
                        "last_name": "Lovelace",
                        "email": "ada@example.com",
                        "phone": "+1-212-555-0199",
                        "birth_date": "1815-12-10",
                        "addresses": [
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440000",
                                "street": "123 Main St",
                                "city": "London",
                                "state": None,
                                "postal_code": "SW1A 1AA",
                                "country": "UK",
                            }
                        ],
                    },
                    "item": "Laptop",
                    "quantity": 2,
                    "price_per_item": 999.99,
                    "order_date": "2023-10-05"
                }
            ]
        }
    }
   
class OrderCreate(OrderBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "customer": {
                        "uni": "abc1234",
                        "first_name": "Ada",
                        "last_name": "Lovelace",
                        "email": "ada@example.com",
                        "phone": "+1-212-555-0199",
                        "birth_date": "1815-12-10",
                        "addresses": [
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440000",
                                "street": "123 Main St",
                                "city": "London",
                                "state": None,
                                "postal_code": "SW1A 1AA",
                                "country": "UK",
                            }
                        ],
                    },
                    "item": "Laptop",
                    "quantity": 2,
                    "price_per_item": 999.99,
                    "order_date": "2023-10-05"
                }
            ]
        }
    }

class OrderUpdate(BaseModel):
    customer: Optional[PersonBase] = Field(
        None,
        description="Customer"
    )
    item: Optional[str] = Field(
        None,
        description="Item being ordered.",
        json_schema_extra={"example": "Laptop"},
    )
    quantity: Optional[int] = Field(
        None,
        description="Quantity of the item ordered.",
        json_schema_extra={"example": 2},
    )
    price_per_item: Optional[float] = Field(
        None,
        description="Price per individual item.",
        json_schema_extra={"example": 999.99},
    )
    order_date: Optional[date] = Field(
        None,
        description="Date when the order was placed (YYYY-MM-DD).",
        json_schema_extra={"example": "2023-10-05"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "customer": {
                        "uni": "abc1234",
                        "first_name": "Ada",
                        "last_name": "Lovelace",
                        "email": "ada@example.com",
                        "phone": "+1-212-555-0199",
                        "birth_date": "1815-12-10",
                        "addresses": [
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440000",
                                "street": "123 Main St",
                                "city": "London",
                                "state": None,
                                "postal_code": "SW1A 1AA",
                                "country": "UK",
                            }
                        ],
                    },
                    "item": "Laptop",
                    "quantity": 2,
                    "price_per_item": 999.99,
                    "order_date": "2023-10-05"
                }
            ]
        }
    }

class OrderRead(OrderBase):
    """Server representation returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Person ID.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config =  {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "customer": {
                        "uni": "abc1234",
                        "first_name": "Ada",
                        "last_name": "Lovelace",
                        "email": "ada@example.com",
                        "phone": "+1-212-555-0199",
                        "birth_date": "1815-12-10",
                        "addresses": [
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440000",
                                "street": "123 Main St",
                                "city": "London",
                                "state": None,
                                "postal_code": "SW1A 1AA",
                                "country": "UK",
                            }
                        ],
                    },
                    "item": "Laptop",
                    "quantity": 2,
                    "price_per_item": 999.99,
                    "order_date": "2023-10-05"
                }
            ]
        }
    }

