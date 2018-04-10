import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('data.txt')

x = datos[:,0]
y = datos[:,1]
x_new = np.linspace(0,10,500)
y_new = np.exp(-x_0)

plt.scatter(x,y)
plt.plot(x_new,y_new)
plt.savefig('grafica1.png')

