import matplotlib.pyplot as plt
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 7, 4, 6, 8])
plt.scatter(arr1, arr2, color='blue', marker='v')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)
plt.show()