from itransfer import ITransfer
from iverify_credit_card import IVerifyCreditCard
from iverify_pay_pal import IVerifyPayPal
from typing import Optional, override

# BankAccount class handle the accounts Bank
class BankAccount(ITransfer, IVerifyCreditCard, IVerifyPayPal):

    def __init__(self, id: str, balance: float, pin_code: str,
                 credit_card_number: Optional[str] = None,
                 paypal_email: Optional[str] = None, ):
        """
        Constractor
        :param id:
        :param balance:
        :param pin_code:
        :param credit_card_number:
        :param paypal_email:
        "parm: transaction_history:
        """

        self.__id = id # hold ID account
        self.__balance = balance # Hold the balance
        self.__credit_card_number = credit_card_number # Hold the number Credit Card
        self.__paypal_email = paypal_email # Hold PayPal Mail
        self.__pin_code = pin_code # Hold the secret code of credit Card
        self.__transaction_history = [] # hold list Transaction of each user
        print(self)

    @property
    def id(self)-> str:
        """Get the id"""
        return self.__id

    @property
    def balance(self)-> float:
        """Get the balance"""
        return  self.__balance

    @property
    def credit_card_number(self)-> Optional[str]:
        """Get the credit_card_number"""
        return self.__credit_card_number

    @property
    def pin_code(self)-> str:
        """Get the pin_code"""
        return self.__pin_code

    @property
    def paypal_email(self)-> str:
        """Get the paypal_email"""
        return self.__paypal_email

    @property
    def transaction_history(self) -> list:
        """Get copy of transaction history"""
        return self.__transaction_history.copy()

    @balance.setter
    def balance(self, value: float)-> None:
        """
        Set balance
        Raises:
            ValueError: If amount value bigger than Balance, Balance cannot be negative
        """
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    @override
    def transfer(self, amount: float, to_account: 'BankAccount', payment_method: str = "direct")-> None:
        """
        Set Transfer
        :param amount:
        :param to_account:
        :param payment_method:
        :return: None:
        Raises:
            ValueError: If Transfer amount must be positive
            TypeError: Destination must be a BankAccount instance
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if not isinstance(to_account, BankAccount):
            raise TypeError("Destination must be a BankAccount instance")

        if self.__balance >= amount:
            self.__balance -= amount
            to_account.balance += amount

            # Transfer successfully write it in from account Transaction History
            self._add_transaction("transfer_out", amount, {
                "to_account": to_account.id,
                "status": "success",
                "payment_method": payment_method
            })

            # Transfer successfully write it in to account Transaction History
            to_account._add_transaction("transfer_in", amount, {
                "from_account": self.id,
                "status": "success",
                "payment_method": payment_method
            })
            return True
        else:
            # Transaction Failed write it in to account Transaction History
            self._add_transaction("failed_transfer_out", amount, {
                "to_account": to_account.id,
                "status": "failed",
                "payment_method": payment_method,
                "error": "Insufficient funds"
            })
            return False

        # When methode Process are failed we need to write it in Transaction
    def fail_transfer(self, amount: float, to_account: Optional['BankAccount'], payment_method: str = "direct",
                      error: str = ""):
        """
        Handle adapter helper failed transfer, Send Transaction History
        :param amount:
        :param to_account:
        :param payment_method:
        :param error:
        :return: None
        """
        to_account_id = to_account.id if to_account is not None else "unknown"

        # Transfer Failed write it in to account Transaction History
        self._add_transaction("failed_transfer_out", amount, {
            "to_account": to_account_id,
            "status": "failed",
            "payment_method": payment_method,
            "error": error,
            "direction": "outgoing"
        })

        # If from account valid write the failed transaction also at from account
        if to_account is not None:
            to_account._add_transaction("failed_transfer_in", amount, {
                "from_account": self.id,
                "status": "failed",
                "payment_method": payment_method,
                "error": error,
                "direction": "incoming"
            })

    @override
    # returns True if matches internal number
    def verify_credit_card(self, card_number: str)-> bool:
        """
        returns True if matches internal number
        :param card_number:
        :return: boolean:
        """
        if not isinstance(card_number, str):
            return False
        if self.__credit_card_number is None:
            return False
        return self.__credit_card_number == card_number

    @override
    # returns True if matches internal email
    def verify_paypal_email(self, email: str)-> bool:
        """
        returns True if matches internal email
        :param email:
        :return: boolean:
        """
        if not isinstance(email, str):
            return False
        if self.__paypal_email is None:
            return False
        return self.__paypal_email.lower() == email.lower()

    # Feature to allow the user to take money from ATM
    def withdraw_cash(self, amount: float, card_number: str, pin_code: str)-> bool:
        """
        Feature to allow the user to take money from ATM
        :param amount:
        :param card_number:
        :param pin_code:
        :return boolean:
        """
        if amount <= 0:
            return False
        if not isinstance(card_number, str) or not isinstance(pin_code, str):
            return False
        if self.__credit_card_number is None and self.__pin_code is None:
            return False

        if self.__credit_card_number == card_number and self.__pin_code == pin_code:
            if self.balance >= amount:
                self.__balance -= amount

                self._add_transaction("withdraw", amount, {
                    "card_last_4": card_number[-4:],
                    "status": "success"
                })

                return True
            else:
                raise ValueError("Insufficient balance")
        return False

    # Feature to deposit
    def deposit(self, amount: float, card_number: str, pin_code: str) -> bool:
        """
        Deposit Money
        :param amount:
        :param card_number:
        :param pin_code:
        :return boolean:
        """
        if not isinstance(card_number, str) or not isinstance(pin_code, str):
            return False
        if self.__credit_card_number is None and self.__pin_code is None:
            return False

        if self.__credit_card_number == card_number and self.__pin_code == pin_code:
            self.__balance += amount
            self._add_transaction("deposit", amount, {
                "card_last_4": card_number[-4:],
                "status": "success"
            })
            return True
        return False


    # Add transaction to history
    def _add_transaction(self, transaction_type: str, amount: float, details: dict = None)-> None:
        """
        Add transaction to history
        :param transaction_type:
        :param amount:
        :param details:
        :return None:
        """
        from datetime import datetime

        transaction = {
            "type": transaction_type,
            "amount": amount,
            "timestamp": datetime.now().isoformat(),
            "balance_after": self.__balance,
            "details": details or {}
        }
        self.__transaction_history.append(transaction)

    def __str__(self) -> str:
        return (f"BankAccount(id='{self.__id}', "
                f"balance={self.__balance}, "
                f"credit_card_number='{self.__credit_card_number}', "
                f"paypal_email='{self.__paypal_email}')")

    def __eq__(self, other) -> bool:
        if not isinstance(other, BankAccount):
            return False
        return self.__id == other.__id

