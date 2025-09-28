# Завдання 1
# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.


class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self,amount):
        print(f"Оплата карткою{amount}, {self.currency}")


class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self,amount):
        print(f"Оплата PayPall {amount}, {self.currency}")

class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self,amount):
        print(f"оплата криптогаманцем {amount} {self.currency}")

def create_payment():
    print("Оберіть  платіж:")
    print("1. CreditCardPayment")
    print("2. PayPalPayment")
    print("3. CryptoPayment")

    choice = input("Введіть номер (1-3): ")
    currency = input("Введіть свою  валюту : ").upper()

    if choice == "1":
        return CreditCardPayment(currency)
    elif choice == "2":
        return PayPalPayment(currency)
    elif choice == "3":
        return CryptoPayment(currency)
    else :
        print("None")
        return

payments_list = []

for i in range(3):
        print(f"Платіж  {i+1}")
        payment = create_payment()
        if payment:
            payments_list.append(payment)

payments_list.append(CreditCardPayment(""))

test_amounts = []

for i, payment in enumerate(payments_list):
    payment.pay(test_amounts[i])




