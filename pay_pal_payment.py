from typing import override
from payment import Payment
from iverify_pay_pal import IVerifyPayPal


class PayPalPayment(Payment):

    def __init__(self, amount: float, from_account_id: str,
                 to_account_id: str, email: str):

        super().__init__(amount, from_account_id, to_account_id)
        """
        Constractor
        :param amount:
        :param from_account_id:
        :param to_account_id:
        :param card_number:
        """
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a non-empty string")

        self.__email = email

    @property
    def email(self) -> str:
        """Get the email"""
        return self.__email

    @override
    def process(self, accounts: dict) -> bool:
        """
        Check if Exist full condition for Transaction
        If it does make transaction
        :param accounts:
        :return boolean:
        Raises:
             TypeError: Accounts parameter must be a dictionary
        """
        if not isinstance(accounts, dict):
            raise TypeError("Accounts parameter must be a dictionary")

        # Retrieve source account
        from_account = accounts.get(self.from_account_id)
        if from_account is None:
            return False

        # Check PayPal support
        if not isinstance(from_account, IVerifyPayPal):
            from_account.fail_transfer(self.amount, None, "PayPal", "Account does not support PayPal")
            return False

        # Verify PayPal email
        if not from_account.verify_paypal_email(self.email):
            to_account = accounts.get(self.to_account_id)
            from_account.fail_transfer(self.amount, to_account, "PayPal", "Invalid PayPal email")
            return False

        # Retrieve destination account
        to_account = accounts.get(self.to_account_id)
        if to_account is None:
            from_account.fail_transfer(self.amount, None, "PayPal", "Destination account not found")
            return False

        # create transfer
        success = from_account.transfer(self.amount, to_account, "PayPal")
        return success

    def __str__(self) -> str:

        return (f"PayPalPayment(amount={self.amount}, "
                f"from={self.from_account_id}, "
                f"to={self.to_account_id}, "
                f"email={self.__email})")