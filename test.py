from abc import ABC, abstractmethod
from typing import Optional, override


class Payment(ABC):

    def __init__(self, amount: float, from_account_id, to_account_id):
        self.__amount = amount
        self.__from_account_id = from_account_id
        self.__to_account_id = to_account_id

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def from_account_id(self) -> float:
        return self.__from_account_id

    @property
    def to_account_id(self) -> float:
        return self.__to_account_id

    @abstractmethod
    def process(self, accounts: dict)-> bool:
        pass

class CreditCardPayment(Payment):

    def __init__(self, amount: float, from_account_id: str,
                 to_account_id: str, card_number: str):
        super().__init__(amount, from_account_id, to_account_id)
        self.__card_number = card_number
        print(self)

    @property
    def card_number(self) -> str:
        """Get the credit card number."""
        return self.__card_number

    def __str__(self)->str:
        return (
            f"card_number = {self.__card_number}, "
            f"CreditCardPayment amount = {self.amount}, "
            f"from = {self.from_account_id}, "
            f"to = {self.to_account_id}"
        )

    @override
    def process(self, accounts: dict) -> bool:

        # Retrieve source account
        from_account = accounts.get(self.from_account_id)
        print(f" Step 2: Retrieved from_account = {from_account}")

        # Verify card number
        print(f" Step 5: Verifying card number {self.card_number}...")
        if not from_account.verify_credit_card(self.card_number):
            print(" Step 6: Credit card verification failed.")
            return False
        else:
            return True

class IVerifyCreditCard(ABC):

    @abstractmethod
    def verify_credit_card(self, card_number: str) -> bool:
        pass

class BankAccount(IVerifyCreditCard):

    def __init__(self, id: str, balance: float,
                 credit_card_number: Optional[str] = None,
                 paypal_email: Optional[str] = None):

        self.__id = id
        self.__balance = balance
        self.__credit_card_number = credit_card_number
        self.__paypal_email = paypal_email
        print(self)

    @property
    def id(self)-> str:
        return self.__id

    @property
    def balance(self)-> float:
        return  self.__balance

    @property
    def credit_card_number(self)-> Optional[str]:
        return self.__credit_card_number

    @property
    def paypal_email(self)-> str:
        return self.__paypal_email

    @balance.setter
    def balance(self, value: float)-> None:
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    @override
    # returns True if matches internal number
    def verify_credit_card(self, card_number: str)-> bool:
        if not isinstance(card_number, str):
            return False
        if self.__credit_card_number is None:
            return False
        return self.__credit_card_number == card_number

    def __str__(self) -> str:
        return (f"BankAccount(id='{self.__id}', "
                f"balance={self.__balance}, "
                f"credit_card_number='{self.__credit_card_number}', "
                f"paypal_email='{self.__paypal_email}')")

print ("create account")
accounts = {
    "A001": BankAccount("A001", 1000.0, credit_card_number="1234567890123456", paypal_email="user1@example.com"),
    "A002": BankAccount("A002", 500.0, credit_card_number="1111222233334444", paypal_email="user2@example.com")
}

print("create payment")
payments = [
    CreditCardPayment(200.0, "A001", "A002", card_number="1234567890123457"),  # valid
]

for payment in payments:
    print("payment in payments process(accounts)")
    print(payment.process(accounts))
    print("-" * 40)
