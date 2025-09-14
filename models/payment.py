from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import date, datetime
from .person import PersonBase


class PaymentBase(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Persistent Address ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )

    sender: PersonBase = Field(
        None,
        description="Sending Person",
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

    receiver: PersonBase = Field(
        None,
        description="Receiving Person",
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

    amount: float = Field(
        ...,
        description="Payment amount.",
        json_schema_extra={"example": 150.75},
    )
    currency: str = Field(
        ...,
        description="Currency code (e.g., USD, EUR).",
        json_schema_extra={"example": "USD"},
    )
    status: str = Field(
        ...,
        description="Payment status (e.g., pending, completed).",
        json_schema_extra={"example": "completed"},
    )
    method: str = Field(
        ...,
        description="Payment method (e.g., credit card, bank transfer).",
        json_schema_extra={"example": "credit card"},
    )
    birth_date: Optional[date] = Field(
        None,
        description="Date of birth (YYYY-MM-DD).",
        json_schema_extra={"example": "1815-12-10"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "sender": {
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
                    "receiver": {
                        "uni": "xyz5678",
                        "first_name": "Charles",
                        "last_name": "Babbage",
                        "email": "charles@example.com",
                        "phone": "+1-212-555-0123",
                        "birth_date": "1791-12-26",
                        "addresses": [
                            {
                                "id": "123e4567-e89b-12d3-a456-426614174000",
                                "street": "456 High St",
                                "city": "Cambridge",
                                "state": None,
                                "postal_code": "CB2 1TN",
                                "country": "UK",
                            }
                        ],
                    },
                    "amount": 150.75,
                    "currency": "USD",
                    "status": "completed",
                    "method": "credit card",
                    "birth_date": "1815-12-10"
                }
            ]
        }
    }

class PaymentCreate(PaymentBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "sender": {
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
                    "receiver": {
                        "uni": "xyz5678",
                        "first_name": "Charles",
                        "last_name": "Babbage",
                        "email": "charles@example.com",
                        "phone": "+1-212-555-0123",
                        "birth_date": "1791-12-26",
                        "addresses": [
                            {
                                "id": "123e4567-e89b-12d3-a456-426614174000",
                                "street": "456 High St",
                                "city": "Cambridge",
                                "state": None,
                                "postal_code": "CB2 1TN",
                                "country": "UK",
                            }
                        ],
                    },
                    "amount": 150.75,
                    "currency": "USD",
                    "status": "completed",
                    "method": "credit card",
                    "birth_date": "1815-12-10"
                }
            ]
        }
    }



class PaymentUpdate(BaseModel):
    """Partial update model for Payment; only include fields to change."""

    sender: Optional[PersonBase] = Field(
        None,
        description="Sending Person"
    )

    receiver: Optional[PersonBase] = Field(
        None,
        description="Receiving Person"
    )

    amount: Optional[float] = Field(
        None,
        description="Payment amount.",
        json_schema_extra={"example": 150.75},
    )

    currency: Optional[str] = Field(
        None,
        description="Currency code (e.g., USD, EUR).",
        json_schema_extra={"example": "USD"},
    )

    status: Optional[str] = Field(
        None,
        description="Payment status (e.g., pending, completed).",
        json_schema_extra={"example": "completed"},
    )

    method: Optional[str] = Field(
        None,
        description="Payment method (e.g., credit card, bank transfer).",
        json_schema_extra={"example": "credit card"},
    )

    birth_date: Optional[date] = Field(
        None,
        description="Date of birth (YYYY-MM-DD).",
        json_schema_extra={"example": "1815-12-10"},
    )


class PaymentRead(PaymentBase):
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

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "sender": {
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
                    "receiver": {
                        "uni": "xyz5678",
                        "first_name": "Charles",
                        "last_name": "Babbage",
                        "email": "charles@example.com",
                        "phone": "+1-212-555-0123",
                        "birth_date": "1791-12-26",
                        "addresses": [
                            {
                                "id": "123e4567-e89b-12d3-a456-426614174000",
                                "street": "456 High St",
                                "city": "Cambridge",
                                "state": None,
                                "postal_code": "CB2 1TN",
                                "country": "UK",
                            }
                        ],
                    },
                    "amount": 150.75,
                    "currency": "USD",
                    "status": "completed",
                    "method": "credit card",
                    "birth_date": "1815-12-10"
                }
            ]
        }
    }
