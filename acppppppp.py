import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,23,1)
y1=(2*x)+1
y2=(2*x**x)+2
plt.plot(x,y1, linestyle='dashed',marker='D')
plt.plot(x,y2, linestyle='dashed',marker='D')
plt.title('velocity-Time Graph')
plt.xlabel('velocitym/s')
plt.xlabel('time')
plt.legend()
plt.show()