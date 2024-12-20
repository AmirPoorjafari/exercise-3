import math
import matplotlib.pyplot as plt
import numpy as np

def tozi_gusi(x, u, q):
    return (1 / (math.sqrt(2 * math.pi) * q))*math.exp(-((x - u) ** 2) / (2 * q ** 2))


x1 = np.linspace(-5, 5, 400)
y = [tozi_gusi(x, 0, 1) for x in x1]



plt.plot(x1, y, color='black', label='Density Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(-0.001, 0.005)  
plt.grid()
plt.legend()
plt.show()