import math

class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Шаг s не может стать меньше или равен 1")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        moves = max(math.ceil(dx / self.s), math.ceil(dy / self.s))
        return moves

turtle = Turtle(0, 0, 2)

turtle.go_up()
print(f"Позиция после go_up(): ({turtle.x}, {turtle.y})") 

turtle.go_right()
print(f"Позиция после go_right(): ({turtle.x}, {turtle.y})") 

turtle.evolve()
print(f"Текущий шаг после evolve(): {turtle.s}")

turtle.degrade()
print(f"Текущий шаг после degrade(): {turtle.s}") 

print(f"Минимальное количество шагов до (6, 6): {turtle.count_moves(6, 6)}") 