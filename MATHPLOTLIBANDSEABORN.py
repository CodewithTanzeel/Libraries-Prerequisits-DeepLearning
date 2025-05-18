import matplotlib.pyplot as plt
import seaborn as sns

# Line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()

# Scatter plot
plt.scatter(df['Age'], df['Salary'])
plt.show()

# Histogram
plt.hist(df['Age'], bins=5)
plt.show()

# Seaborn for advanced visualization
sns.pairplot(df)  # Pairwise relationships
sns.heatmap(df.corr(), annot=True)  # Correlation heatmap