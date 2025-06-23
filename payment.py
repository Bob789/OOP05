from abc import ABC, abstractmethod

class Payment(ABC):
    """
    Abstract interface for methode payment
    """

    def __init__(self, amount: float, from_account_id, to_account_id):
        """
        Constractor
        :param amount:
        :param from_account_id:
        :param to_account_id:
        :Raise:
            ValueError: Payment amount must be positive
            TypeError: Account IDs must be strings
        """

        if amount <= 0:
            raise ValueError("Payment amount must be positive")
        if not isinstance(from_account_id, str) or not isinstance(to_account_id, str):
            raise TypeError("Account IDs must be strings")
        self.__amount = amount
        self.__from_account_id = from_account_id
        self.__to_account_id = to_account_id

    @property
    def amount(self) -> float:
        """Get the amount"""
        return self.__amount

    @property
    def from_account_id(self) -> str:
        """Get the from_account_id"""
        return self.__from_account_id

    @property
    def to_account_id(self) -> str:
        """Get the to_account_id"""
        return self.__to_account_id

    @abstractmethod
    def process(self, accounts: dict)-> bool:
        """
        Interface methode for
        Check if Exist full condition for Transaction
        If it does make transaction
        :param accounts:
        :return boolean:
        """
        pass

    def __str__(self) -> str:

        return (f"Payment(amount={self.__amount}, "
                f"from={self.__from_account_id}, "
                f"to={self.__to_account_id})")