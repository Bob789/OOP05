from abc import ABC, abstractmethod

class IVerifyCreditCard(ABC):
    """
    Abstract interface for Verify Credit Card
    """
    @abstractmethod
    def verify_credit_card(self, card_number: str) -> bool:
        """
         Check if Credit card are valid
         :parm card_number:
         :return boolean:
        """
        pass