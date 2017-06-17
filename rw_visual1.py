
import matplotlib.pyplot as plt
from random_walk1 import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    pint_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = pint_numbers, cmap = plt.cm.Blues, edgecolor="none", s=15)
    plt.show()

    '''make mutiple random walk'''

    prompt = input("do you want to randomly walk again?(Y/N)")
    if prompt == "N":
        break
