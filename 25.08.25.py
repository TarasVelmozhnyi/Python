#Завдання 1
# Напишіть клас Банківський рахунок з атрибутами:
#  ім'я клієнта
#  баланс
#  валюта
#  словник з курсом валют(однаковий для всіх)
# Додайте методи:
#  вивід загальної інформації
#  перевірка чи відома валюта(якщо ні, викликати
# ValueError)
#  перевести гроші з однієї валюти в іншу(ця операція
# часто використовується, тому зрочно реалізувати
# окремим методом)
#  зміна валюти
#  поповнення балансу(валюта та сама)
#  зняття грошей з балансу(валюта та сама).



class BankAccount:
    exchange_rates = {
        'UAH': {'USD': 0.025, 'EUR': 0.023},
        'USD': {'UAH': 40.0, 'EUR': 0.92},
        'EUR': {'UAH': 43.5, 'USD': 1.09}
    }

    def __init__(self, client_name, balance=0, currency='UAH'):
        self.client_name = client_name
        self.balance = balance
        self.currency = currency

        self._validate_currency(currency)

    def _validate_currency(self, currency):

        if currency not in self.exchange_rates:
            raise ValueError(f"Невідома валюта: {currency}")

    def display_info(self):

        print(f"Ім'я клієнта: {self.client_name}")
        print(f"Баланс: {self.balance:.2f} {self.currency}")
        print(f"Валюта рахунку: {self.currency}")

    def convert_currency(self, amount, from_currency, to_currency):

        self._validate_currency(from_currency)
        self._validate_currency(to_currency)

        if from_currency == to_currency:
            return amount

        if to_currency not in self.exchange_rates[from_currency]:
            raise ValueError(f"Неможливо конвертувати з {from_currency} в {to_currency}")

        rate = self.exchange_rates[from_currency][to_currency]
        return amount * rate

    def change_currency(self, new_currency):

        self._validate_currency(new_currency)

        if self.currency != new_currency:
            self.balance = self.convert_currency(self.balance, self.currency, new_currency)
            self.currency = new_currency
            print(f"Валюта рахунку змінена на {new_currency}")
        else:
            print("Валюта вже встановлена на цю валюту")

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Сума поповнення повинна бути більше 0")

        self.balance += amount
        print(f"Рахунок поповнено на {amount:.2f} {self.currency}")
        print(f"Новий баланс: {self.balance:.2f} {self.currency}")

    def withdraw(self, amount):

        if amount <= 0:
            print("Сума зняття повинна бути більше 0")
            return

        if amount > self.balance:
            print("Недостатньо коштів на рахунку")
            return

        else:
            self.balance -= amount
            print(f"З рахунку знято {amount:.2f} {self.currency}")
            print(f" баланс: {self.balance:.2f} {self.currency}")




account1 = BankAccount("Іван Петренко", 1000, "UAH")
account1.display_info()
account1.deposit(500)
account1.withdraw(200)
usd_amount = account1.convert_currency(100, "UAH", "USD")
print(f"100 UAH = {usd_amount:.2f} USD")
account1.change_currency("UAH")
account1.display_info()
account2 = BankAccount("Марія Коваленко", 500, "EUR")
account2.display_info()

try:
    account3 = BankAccount("Петро Сидоренко", 1000, "GBP")
except ValueError as e:
    print(f"\nПомилка: {e}")