from matplotlib import pyplot as plt
import numpy as np
X = np.array([-4,3,-2.25])
Y = np.array([2,6,3])
plt.plot(X,Y,"-s",label='$7y=4x+30$')
plt.savefig("fig1.png")
plt.annotate('A(-4,2)',(-4,2),xytext=(-3.8,1.95))
plt.annotate('B(3,6)',(3,6),xytext=(2.3,5.95))
plt.annotate('P(-2.25,3)',(-2.25,3),xytext=(-2,2.95))
plt.legend(loc='best', prop={'size':11})
plt.grid()
plt.show()
print('hi')