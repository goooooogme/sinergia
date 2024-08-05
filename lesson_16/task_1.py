class Kassa:
    def __init__(self):
        self.balance = 0

    def top_up(self, X):
        if X > 0:
            self.balance += X
        else:
            raise ValueError("Сумма пополнения должна быть положительным числом")

    def count_1000(self):
        return self.balance // 1000 

    def take_away(self, X):
        if X > 0:
            if X <= self.balance:
                self.balance -= X
            else:
                raise ValueError("Недостаточно денег в кассе")
        else:
            raise ValueError("Сумма снятия должна быть положительным числом")

kassa = Kassa()

kassa.top_up(5000)
print(f"Баланс после пополнения: {kassa.balance}") 

print(f"Количество целых тысяч: {kassa.count_1000()}") 

kassa.take_away(3000)
print(f"Баланс после снятия: {kassa.balance}")  

print(f"Количество целых тысяч: {kassa.count_1000()}")  

try:
    kassa.take_away(2500)
except ValueError as e:
    print(e)