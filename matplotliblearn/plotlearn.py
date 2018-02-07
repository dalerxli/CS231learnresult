"""
matplotlib绘图功能
create by swm
2018/02/07
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('Sine')
# Set the second subplot as active
plt.subplot(2, 1, 1)
plt.plot(x, y_cos)
plt.title('Cosine')

plt.subplot(2, 1, 2)
plt.plot(x, y_tan)
plt.title('tan')

# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.plot(x, y_tan)
# plt.xlabel('x axis lable')
# plt.ylabel('y axis label')
# plt.title('linear math')
# plt.legend(['Sine', 'Cosine'])
plt.show()