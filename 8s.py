class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self._owner = owner
        self._balance = initial_balance
        self._transaction_count = 0
    @property
    def owner(self):
        return self._owner
    @property
    def balance(self):
        return self._balance
    @property
    def transaction_count(self):
        return self._transaction_count
    @property
    def is_overdraft(self):
        return self._balance < 0
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance += amount
        self._transaction_count += 1
        print(f"Внесено: {amount}. Новый баланс: {self._balance}")
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете")
        self._balance -= amount
        self._transaction_count += 1
        print(f"Снято: {amount}. Новый баланс: {self._balance}")
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля (-273.15°C)")
        self._celsius = value
    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9
    @property
    def kelvin(self):
        return self._celsius + 273.15
    @kelvin.setter
    def kelvin(self, value):
        if value < 0:
            raise ValueError("Температура в Кельвинах не может быть отрицательной")
        self._celsius = value - 273.15
class Rectangle:
    def __init__(self, width, height):
        if width <= 0:
            raise ValueError("Ширина должна быть положительной")
        if height <= 0:
            raise ValueError("Высота должна быть положительной")
        self._width = width
        self._height = height
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Ширина должна быть положительной")
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Высота должна быть положительной")
        self._height = value
    @property
    def area(self):
        return self._width * self._height
    @property
    def perimeter(self):
        return 2 * (self._width + self._height)
if __name__ == "__main__":
    print("=== Демонстрация BankAccount с property ===\n")
    account = BankAccount("Иван Иванов", 1000)
    print(f"Владелец: {account.owner}")
    print(f"Начальный баланс: {account.balance}")
    print(f"Количество транзакций: {account.transaction_count}")
    print(f"Овердрафт: {account.is_overdraft}")
    account.deposit(500)
    account.withdraw(200)
    print(f"Итоговый баланс: {account.balance}")
    print(f"Всего транзакций: {account.transaction_count}")
    print("\n" + "=" * 50 + "\n")
    print("=== Демонстрация Temperature с property ===\n")
    temp = Temperature(25)
    print(f"Температура: {temp.celsius}°C")
    print(f"Температура: {temp.fahrenheit}°F")
    print(f"Температура: {temp.kelvin}K")
    temp.celsius = 30
    print(f"После установки 30°C: {temp.fahrenheit}°F")
    temp.fahrenheit = 100
    print(f"После установки 100°F: {temp.celsius}°C")
    temp.kelvin = 300
    print(f"После установки 300K: {temp.celsius}°C")
    print("\n" + "=" * 50 + "\n")
    print("=== Демонстрация Rectangle с property ===\n")
    rect = Rectangle(5, 3)
    print(f"Прямоугольник: {rect.width}x{rect.height}")
    print(f"Площадь: {rect.area}")
    print(f"Периметр: {rect.perimeter}")
    rect.width = 8
    rect.height = 4
    print(f"После изменения: {rect.width}x{rect.height}")
    print(f"Новая площадь: {rect.area}")
    print(f"Новый периметр: {rect.perimeter}")
    print("\n" + "=" * 50 + "\n")
    print("=== Демонстрация валидации ===\n")
    try:
        rect.width = -5
    except ValueError as e:
        print(f"Ошибка при установке ширины: {e}")
    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"Ошибка при установке температуры: {e}")