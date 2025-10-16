class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value
    def increment(self, step=1):
        self.value += step
    def decrement(self, step=1):
        self.value -= step
    def reset(self, new_value=0):
        self.value = new_value
    def __str__(self):
        return f"Счётчик: {self.value}"
if __name__ == "__main__":
    counter = Counter(10)
    print(counter)
    counter.increment()
    print(f"После увеличения: {counter}")
    counter.increment(5)
    print(f"После увеличения на 5: {counter}")
    counter.decrement()
    print(f"После уменьшения: {counter}")
    counter.decrement(3)
    print(f"После уменьшения на 3: {counter}")
    counter.reset()
    print(f"После сброса: {counter}")
    counter.reset(100)
    print(f"После сброса в 100: {counter}")