import matplotlib.pyplot as plt
import numpy as np
ages = np.random.randint(18, 60, 1000)
plt.hist(ages, bins=8, color='purple', edgecolor='black')
plt.title('Age Distribution of Participants')
plt.xlabel('Age')
plt.ylabel('Number of Participants')
plt.show()
