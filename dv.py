import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
months = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
temps = [24, 25, 28, 30, 32, 35, 36, 35, 33, 30, 27, 25]
df = pd.DataFrame({'Month': months, 'Temperature': temps})
plt.plot(df['Month'], df['Temperature'], marker='o')
plt.title('Average Monthly Temperatures')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)') 
plt.grid(True)
plt.xticks(rotation=45)
plt.show()