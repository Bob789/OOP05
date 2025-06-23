from typing import override
from iverify_credit_card import IVerifyCreditCard
from payment import Payment


class CreditCardPayment(Payment):

    def __init__(self, amount: float, from_account_id: str,
                 to_account_id: str, card_number: str):
        super().__init__(amount, from_account_id, to_account_id)
        """
        Constractor
        :param amount:
        :param from_account_id:
        :param to_account_id:
        :param card_number:
        """

        if not card_number or not isinstance(card_number, str):
            raise ValueError("Card number must be a non-empty string")
        self.__card_number = card_number

    @property
    def card_number(self) -> str:
        """Get the credit card number"""
        return self.__card_number

    @override
    def process(self, accounts: dict) -> bool:
        """
        Check if Exist full condition for Transaction
        If it does make transaction
        :param accounts:
        :return boolean:
        Raises
            TypeError: Accounts parameter must be a dictionary
        """
        if not isinstance(accounts, dict):
            raise TypeError("Accounts parameter must be a dictionary")

        # Retrieve source account
        from_account = accounts.get(self.from_account_id)

        # check source account if not found
        if from_account is None:
            return False

        # Check if source account support credit card verification
        if not isinstance(from_account, IVerifyCreditCard):
            return False

        # Verify card number
        if not from_account.verify_credit_card(self.card_number):
            print(" Credit card verification failed.")
            return False

        # Retrieve destination account
        to_account = accounts.get(self.to_account_id)

        # Destination account not found
        if to_account is None:
            return False

        # Transferring amount between two accounts
        success = from_account.transfer(self.amount, to_account, "Credit Card")
        return success

    def __str__(self) -> str:
        """
        Return a string representation of the credit card payment.

        Returns:
            str: Formatted payment information with masked card number.
        """
        # Mask all but last 4 digits for security
        print("last 4 digits for security")
        masked_card = "*" * (len(self.__card_number) - 4) + self.__card_number[-4:]
        return (f"CreditCardPayment(amount={self.amount}, "
                f"from={self.from_account_id}, "
                f"to={self.to_account_id}, "
                f"card={masked_card})")