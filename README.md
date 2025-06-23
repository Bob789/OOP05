# Banking System - README

## מה עושה התוכנית:

מערכת המדמה העברת כספים בין חשבונות בנק תוך שימוש בכרטיס אשראי או PayPal.
ניתן לבצע העברות כספים, הפקדות, משיכות ופעולות אימות לכרטיסי אשראי וחשבונות PayPal.

---

## סיכום מבנה התוכנית לפי קבצים:

### bank\_account.py - מחלקה BankAccount

* ירושה מהממשקים: `ITransfer`, `IVerifyCreditCard`, `IVerifyPayPal`
* ניהול חשבון בנק עם אפשרות העברת כספים, הפקדות, משיכות ורישום היסטוריית פעולות
* אימות כרטיס אשראי ו-PayPal

### payment.py - מחלקה אבסטרקטית Payment

* מייצגת תשלום כללי
* מחייבת מימוש פונקציית `process`

### credit\_card\_payment.py - מחלקה CreditCardPayment

* ירושה מ-`Payment`
* תשלום באמצעות כרטיס אשראי כולל אימות

### pay\_pal\_payment.py - מחלקה PayPalPayment

* ירושה מ-`Payment`
* תשלום באמצעות PayPal כולל אימות

### itransfer.py - ממשק ITransfer

* מחייב מימוש מתודת `transfer` להעברת כספים

### iverify\_credit\_card.py - ממשק IVerifyCreditCard

* מחייב מימוש מתודת `verify_credit_card`

### iverify\_pay\_pal.py - ממשק IVerifyPayPal

* מחייב מימוש מתודת `verify_paypal_email`

### main.py

* יצירת חשבונות, ביצוע תשלומים שונים, הדפסת היסטוריית פעולות

---

## UML תרשים:

```
           +----------------+
           |    Payment     |<---------------------+  
           +----------------+                      |
            ^                ^                    |
+-------------------+  +-------------------+      |
| CreditCardPayment |  |   PayPalPayment   |      |
+-------------------+  +-------------------+      |
           ^                         ^            |
           |                         |            |
+------------------+      +-------------------+   |
|   BankAccount    |<------+ IVerifyPayPal    |   |
+------------------+      +-------------------+   |
       ^      ^                  ^                |
       |      |                  +----------------+
+-------------+-----------------+
| ITransfer   | IVerifyCreditCard |
+-------------+-----------------+
```

---

## עיקרי פונקציות:

* `transfer` - העברת כספים בין חשבונות
* `verify_credit_card` - אימות כרטיס אשראי
* `verify_paypal_email` - אימות כתובת PayPal
* `withdraw_cash` - משיכת מזומן
* `deposit` - הפקדת מזומן
* `process` (ב-Payment) - עיבוד תשלום, יש מימוש לכל סוג תשלום
* `_add_transaction` - הוספת רשומה להיסטוריית הפעולות

```
OutPut
create accounts Bank, start position
BankAccount(id='A001', balance=1000.0, credit_card_number='1234567890123456', paypal_email='user1@example.com')
BankAccount(id='A002', balance=500.0, credit_card_number='1111222233334444', paypal_email='user2@example.com')
BankAccount(id='A003', balance=2750.0, credit_card_number='5555666677778888', paypal_email='user3@example.com')
create payment
True
------------------------------------------------
False
------------------------------------------------
False
------------------------------------------------

Additional functionality - Handling withdraw cash
Send SMS
Withdraw cash are done successfully

Additional functionality - Handling deposit cash
Send SMS
Deposit cash are done successfully

===========================
=== Transaction History ===
BankAccount(id='A001', balance=800.0, credit_card_number='1234567890123456', paypal_email='user1@example.com')
1. {'type': 'transfer_out', 'amount': 200.0, 'timestamp': '2025-06-23T12:45:06.577015', 'balance_after': 800.0, 'details': {'to_account': 'A002', 'status': 'success', 'payment_method': 'Credit Card'}}
2. {'type': 'failed_transfer_out', 'amount': 300.0, 'timestamp': '2025-06-23T12:45:06.578020', 'balance_after': 800.0, 'details': {'to_account': 'A002', 'status': 'failed', 'payment_method': 'PayPal', 'error': 'Invalid PayPal email', 'direction': 'outgoing'}}
===========================
=== Transaction History ===
BankAccount(id='A002', balance=700.0, credit_card_number='1111222233334444', paypal_email='user2@example.com')
1. {'type': 'transfer_in', 'amount': 200.0, 'timestamp': '2025-06-23T12:45:06.578020', 'balance_after': 700.0, 'details': {'from_account': 'A001', 'status': 'success', 'payment_method': 'Credit Card'}}
2. {'type': 'failed_transfer_in', 'amount': 300.0, 'timestamp': '2025-06-23T12:45:06.578020', 'balance_after': 700.0, 'details': {'from_account': 'A001', 'status': 'failed', 'payment_method': 'PayPal', 'error': 'Invalid PayPal email', 'direction': 'incoming'}}
3. {'type': 'failed_transfer_out', 'amount': 900.0, 'timestamp': '2025-06-23T12:45:06.578020', 'balance_after': 700.0, 'details': {'to_account': 'A001', 'status': 'failed', 'payment_method': 'Credit Card', 'error': 'Insufficient funds'}}
===========================
=== Transaction History ===
BankAccount(id='A003', balance=2333.0, credit_card_number='5555666677778888', paypal_email='user3@example.com')
1. {'type': 'withdraw', 'amount': 750.0, 'timestamp': '2025-06-23T12:45:06.578020', 'balance_after': 2000.0, 'details': {'card_last_4': '8888', 'status': 'success'}}
2. {'type': 'deposit', 'amount': 333.0, 'timestamp': '2025-06-23T12:45:06.578020', 'balance_after': 2333.0, 'details': {'card_last_4': '8888', 'status': 'success'}}
```

## דרישות להרצה:

* Python 3.9+
* אין צורך בספריות חיצוניות

## הרצה:

```
python main.py
```

מומלץ לבדוק את הדפסות המסך לצורך הבנת תהליך הפעולה והיסטוריית הטרנזקציות.
