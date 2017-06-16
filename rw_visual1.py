
import matplotlib.pyplot as plt
from random_walk1 import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
