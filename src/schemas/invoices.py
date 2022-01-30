from pydantic import BaseModel
from typing import List, Optional


class InvoiceOrderLineCreate(BaseModel):
    quantity: int
    price: float
    cost: float
    medicine_id: int


class InvoiceOrderLineOut(InvoiceOrderLineCreate):
    id: int
    invoice_id: int

    class Config:
        orm_mode = True


class InvoiceOrderCreate(BaseModel):
    total_amount: float
    paid_amount: float
    due_amount: float
    comment: Optional[str]
    discount: Optional[int]
    vat: Optional[int]
    profit_on_transaction: float = 0
    customer_id: Optional[int]
    user_id: int


class InvoiceOrderOut(InvoiceOrderCreate):
    id: int
    invoice_lines: Optional[List[InvoiceOrderLineOut]] = None

    class Config:
        orm_mode = True
