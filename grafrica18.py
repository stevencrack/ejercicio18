import numpy as np
import matplotlib.pyplot as plt

d=np.loadtxt('data.txt')

x=d[:,0]
y=d[:,1]

x = np.linspace(0,1,500) 
y_0= np.exp(-x)


plt.figure() 
plt.scatter(x,y) 
plt.xlabel("Eje x") 
plt.ylabel("Eje y") 
plt.savefig("grafica1.png")
plt.show()
