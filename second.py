import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('data2.txt')

x = datos[:,0]
y = datos[:,1]
z = datos[:,2]

plt.scatter(y,z)
plt.savefig('second1.png')
plt.show()
plt.scatter(x,y)
plt.savefig('second2.png')
plt.show()
