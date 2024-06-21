import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sales': [150, 200, 250, 300, 350, 400],
    'Profit': [50, 70, 90, 110, 130, 150]
}

df = pd.DataFrame(data)

# Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df['Month'], df['Sales'], color='blue', label='Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales')
plt.legend()
plt.show()

# Line Chart
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Sales'], marker='o', color='blue', label='Sales')
plt.plot(df['Month'], df['Profit'], marker='s', color='green', label='Profit')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Monthly Sales and Profit')
plt.legend()
plt.show()
