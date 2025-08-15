#Дан одномерный массив А размерности N. Найти количество элементов, больших заданного числа В и их произведение.

from dataclasses import dataclass
from typing import Optional, Tuple, List

@dataclass
class GreaterThanStats:
    numbers: List[float]
    B: float
    count: int = 0
    product: Optional[float] = None

    def calculate(self) -> Tuple[int, Optional[float]]:
        self.count = 0
        self.product = None
        for x in self.numbers:
            if x > self.B:
                if self.product is None:
                    self.product = x
                else:
                    self.product *= x
                self.count += 1
        return self.count, self.product

    def __str__(self) -> str:
        prod_str = "None" if self.product is None else str(self.product)
        return f"B={self.B}; count={self.count}; product={prod_str}"


if __name__ == "__main__":
    stats = GreaterThanStats(numbers=[3, -1, 5, 0, -7, 8], B=2)
    stats.calculate()
    print(stats) 

    stats = GreaterThanStats(numbers=[0, 0, 0], B=0)
    stats.calculate()
    print(stats) 

    stats = GreaterThanStats(numbers=[-5, -2, -9], B=-1)
    stats.calculate()
    print(stats) 

    stats = GreaterThanStats(numbers=[1, 2, 3], B=1)
    stats.calculate()
    print(stats) 

    stats = GreaterThanStats(numbers=[10], B=5)
    stats.calculate()
    print(stats) 

    stats = GreaterThanStats(numbers=[5,5,5], B=5)
    stats.calculate()
    print(stats) 

    stats = GreaterThanStats(numbers=[2, -3, 4, -1, 0], B=0)
    stats.calculate()
    print(stats) 

    stats = GreaterThanStats(numbers=[1000000, 1000, 100], B=50)
    stats.calculate()
    print(stats) 

    stats = GreaterThanStats(numbers=[], B=7)
    stats.calculate()
    print(stats) 

    stats = GreaterThanStats(numbers=[-2, -1, 1, 2], B=-5)
    stats.calculate()
    print(stats) 

