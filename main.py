from bank_account import BankAccount
from credit_card_payment import CreditCardPayment
from pay_pal_payment import PayPalPayment

def main():
    print ("create accounts Bank, start position")
    accounts = {
        "A001": BankAccount("A001", 1000.0, "5678", credit_card_number="1234567890123456",
                            paypal_email="user1@example.com"),
        "A002": BankAccount("A002", 500.0, "1234", credit_card_number="1111222233334444",
                            paypal_email="user2@example.com"),
        "A003": BankAccount("A003", 2750.0, "4415", credit_card_number="5555666677778888",
                            paypal_email="user3@example.com")
    }

    print("create payment")
    payments = [
        CreditCardPayment(200.0, "A001", "A002", card_number="1234567890123456"),  # valid
        PayPalPayment(300.0, "A001", "A002", email="wrong@example.com"),           # invalid email
        CreditCardPayment(900.0, "A002", "A001", card_number="1111222233334444")   # insufficient funds
    ]

    for payment in payments:
        print(payment.process(accounts))
        print("-" * 48)

    print()
    print("Additional functionality - Handling withdraw cash")
    success = accounts["A003"].withdraw_cash(750.0, "5555666677778888", "4415")
    print("Send SMS")
    if success:
        print("Withdraw cash are done successfully")
    else:
        print("Your request to withdraw cash are rejected")

    print()
    print("Additional functionality - Handling deposit cash")
    success = accounts["A003"].deposit(333.0, "5555666677778888", "4415")
    print("Send SMS")
    if success:
        print("Deposit cash are done successfully")
    else:
        print("Your request to withdraw cash are rejected")

    print()
    for acc in accounts.values():
        print("=" * 27)
        print("=== Transaction History ===")
        print(acc)
        history = acc.transaction_history

        for i, transaction in enumerate(history, 1):
            print(f"{i}. {transaction}")

if __name__ == "__main__":
    main()