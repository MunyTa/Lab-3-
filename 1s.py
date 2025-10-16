class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
class DatabaseConnection(Singleton):
    def __init__(self, connection_string="default_connection"):
        if not hasattr(self, 'initialized'):
            self.connection_string = connection_string
            self.is_connected = False
            self.initialized = True
            print(f"Создано подключение к базе: {self.connection_string}")
    def connect(self):
        if not self.is_connected:
            self.is_connected = True
            print(f"Подключение к базе: {self.connection_string}")
        else:
            print("Уже подключено!")
    def disconnect(self):
        if self.is_connected:
            self.is_connected = False
            print("Отключение от базы")
        else:
            print("Уже отключено!")
    def __str__(self):
        return f"DatabaseConnection('{self.connection_string}', connected={self.is_connected})"
if __name__ == "__main__":
    print("=== Демонстрация Singleton ===")
    db1 = DatabaseConnection("postgresql://localhost/mydb")
    print(f"db1: {db1}")
    db2 = DatabaseConnection("mysql://localhost/otherdb")
    print(f"db2: {db2}")
    print(f"db1 is db2: {db1 is db2}")
    print(f"ID db1: {id(db1)}")
    print(f"ID db2: {id(db2)}")
    print("\n=== Работа с подключением ===")
    db1.connect()
    db2.connect()
    db1.disconnect()
    db2.disconnect()
    print("\n=== Дополнительная проверка ===")
    db1.connection_string = "Новая строка подключения"
    print(f"db1.connection_string: {db1.connection_string}")
    print(f"db2.connection_string: {db2.connection_string}")