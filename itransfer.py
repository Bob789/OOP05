from abc import ABC, abstractmethod

class ITransfer(ABC):
    """
    Abstract interface for money transfer operations
    """
    @abstractmethod
    def transfer(self, amount: float, to_account: 'BankAccount') -> bool:
        """
        Transfer money from this account to another account
        :param amount:
        :param to_account:
        :return:boolean:
        """
        pass