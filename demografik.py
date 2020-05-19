import matplotlib.pyplot as plt
import numpy as np

# Bounds and step
coeff=4
step = 0.05
bound = coeff * np.pi

#Values of independent variable and functions
x = np.arange(-bound, bound + step, step)
f = np.sin(x)
g = np.cos(x)

# Figures
plt.plot(x, f, x, g)
plt.title('Functions:')
plt.xlabel('X')
plt.ylabel('Y')

plt.grid(True)

plt.show()
