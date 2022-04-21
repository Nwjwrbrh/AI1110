from matplotlib import pyplot as plt
import numpy as np
import math
X = np.linspace(1,0,10000,endpoint=False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(X,np.arcsin(X)+np.arcsin(1-X),label= '$y = \\sin^{-1}x + \\sin^{-1}(1-x)$')
plt.plot(X,np.arccos(X),label='$y = cos^{-1}x$')
plt.plot(0.5,math.pi/3,'o',color='black')
plt.legend(loc='best', prop={'size':10})
plt.grid()
plt.annotate('(0.5,$\pi$/3)',(0.5,math.pi/3),xytext=(0.515,1.1))
plt.savefig("fig2.png")
plt.show()