import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
students_year = ['First Year', 'Second Year', 'Third Year', 'Fourth Year']
num_students = [120, 100, 80, 60]
colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
df = pd.DataFrame({'Year': students_year, 'Number of Students': num_students})
plt.pie(df['Number of Students'], labels=df['Year'],colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Students Across Years')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()