import math
import numpy as np
import matplotlib.pyplot as plt

a = 3
b = 0.5
x = np.arange(-2, 2.001, 0.001)
c = sum((b**i)*np.cos(a**i * np.pi * x) for i in range(0, 100))
plt.plot(x, c)
plt.show()

