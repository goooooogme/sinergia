#Дан одномерный массив А размерности N. Найти сумму положительных элементов и их количество.
class PositiveStats:
    def __init__(self, numbers):
        self.numbers = numbers
        self.total_sum = 0
        self.count = 0

    def calculate(self):
        for num in self.numbers:
            if num > 0:
                self.total_sum += num
                self.count += 1

    def __str__(self):
        return f"Сумма: {self.total_sum}, Количество: {self.count}"

data = PositiveStats([3, -1, 5, 0, -7, 8])
data.calculate()
print(data)