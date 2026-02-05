import random
import matplotlib.pyplot as plt

# X axis values: 1 to 12
x = list(range(1, 13))

# Y axis values: random integers between 0 and 100
y = [random.randint(0, 100) for _ in range(12)]

# Create bar chart
plt.bar(x, y)

# Labels
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Bar Chart with Random Values")

# Show plot
plt.show()