from matplotlib import pyplot as plt

from random import choice

class RandomWalk():
    def __init__(self, dot_quantity=50000):
        self.dot_quantity = dot_quantity
        self.x_positions = [0]
        self.y_positions = [0]

    def walking(self):
        while len(self.x_positions) < self.dot_quantity:
            self.x_direction = choice([1, -1])
            self.x_distance = choice([1, 2, 3, 4, 5])
            self.x_step = self.x_direction * self.x_distance

            self.y_direction = choice([1, -1])
            self.y_distance = choice([1, 2, 3, 4, 5])
            self.y_step = self.y_direction * self.y_distance

            next_x = self.x_positions[-1] + self.x_step
            next_y = self.y_positions[-1] + self.y_step

            if self.x_step == 0 and self.y_step == 0:
                continue

            self.x_positions.append(next_x)
            self.y_positions.append(next_y)

              
rw = RandomWalk()
rw.walking()

plt.scatter(rw.x_positions, rw.y_positions, c=rw.y_positions, edgecolors='none', cmap=plt.cm.Blues, s=1)
plt.scatter(0, 0, c='black', edgecolors='none', s=50)
plt.scatter(rw.x_positions[-1], rw.y_positions[-1], c='red', edgecolors='none', s=50)
plt.title('A random walk', fontsize=20)

plt.show()
