# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик


class Cart:
    def __init__(self, client):
        self.client = client
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f" '{item}' додано до кошика  {self.client}")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Товар '{item}' видалено з кошика  {self.client}")
        else:
            print(f"Товару '{item}' не знайдено в кошику  {self.client}")

    def show_cart(self):
        print(f"кошик клиента {self.client}")
        if self.items:
            for i , item in enumerate(self.items , 1):
                print(f"{i} , {item}")
        else :
            print("кошик порожній")


cart = Cart("Taras")
cart.add_item("milk")
cart.add_item("apple")
cart.show_cart()
cart.remove_item("apple")
cart.show_cart()
cart.remove_item("bread")



# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон


class Phone:
    def __init__(self, number, battery_level=100):
        self.number = number
        self.battery_level = battery_level

    def decrease_battery(self, percent):
        if percent < 0:
            print("Помилка: відсоток не може бути від'ємним")
            return

        self.battery_level -= percent

        if self.battery_level < 0:
            self.battery_level = 0

        if 0 < self.battery_level < 20:
            print(f" Низький заряд батареї: {self.battery_level}")


    def display_info(self):
        print(f"Номер: {self.number}")
        print(f"Заряд батареї:  {self.battery_level}%")


phone = Phone("+380959401149", 80)
phone.display_info()
phone.decrease_battery()
phone.battery_level()
phone.display_info()






