import matplotlib.pyplot as plt
import numpy as np

# Generate some sample age data (like ages of 100 people)
ages = np.random.randint(18, 60, size=100)

# Create histogram
plt.hist(ages, bins=8, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel("Age Groups")
plt.ylabel("Number of People")
plt.title("Distribution of Ages in a Population")

# Show the plot
plt.show()
