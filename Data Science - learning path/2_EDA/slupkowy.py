import matplotlib.pyplot as plt
import random

"""
    Fo every name in names list cast integer lots using randint function from random library
"""

names = ['Ala', 'Ola', 'Kamil', 'Anita', 'Kasia']
points = [ random.randint(5, 20) for name in names]

plt.bar(names, points, color=['red', 'green', 'blue'])
plt.xticks(names)
plt.yticks(points)
plt.show()
