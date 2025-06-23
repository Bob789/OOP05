from abc import ABC, abstractmethod
from typing import override


class IVerifyPayPal(ABC):
    """
    Abstract interface for Email PayPal
    """
    @override
    def verify_paypal_email(self, email: str):
        """
        Check if Email PayPal are valid
        :param email:
        :return boolean:
        """
        pass