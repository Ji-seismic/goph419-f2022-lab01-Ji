import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,50)
y=np.cos(x)
plt.plot(x,y,label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("cos(x)")
plt.show()