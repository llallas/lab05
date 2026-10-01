# Author: Elias Arriaga
# Date: 10/1/2026
# File: invoice.py
# Description:

from payroll.payable import Payable

# Represents an external payment for purchased items with class-level invoice tracking.
class Invoice(Payable):


    _invoice_count = 0

    def __init__(self, part_name: str, price: float, quantity: int):
        self.part_name = part_name
        self.price = price
        self.quantity = quantity
        Invoice._invoice_count += 1

    def calculate_payment(self) -> float:

        return self.price * self.quantity

    def to_dict(self) -> dict:
        return {
            "type": "Invoice",
            "part_name": self.part_name,
            "price": self.price,
            "quantity": self.quantity,
            "payment_amount": self.calculate_payment(),
        }

    @classmethod
    def get_invoice_count(cls) -> int:
        return cls._invoice_count