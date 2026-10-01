# Author: Elias Arriaga
# Date: 2026-10-01
# Name: payable.py
# Description: Defines the abstract Payable interface enforcing calculation and serialization contracts.

from abc import ABC, abstractmethod


class Payable(ABC):
    # Abstract base class representing any entity that can be paid in the system.

    @abstractmethod
    def calculate_payment(self) -> float:

        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass