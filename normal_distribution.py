# This script calculates and plots a Normal Distribution

import numpy as np
import matplotlib.pyplot as plt

# Set the mean and standard deviation
mu = 0    # mean
sigma = 1 # standard deviation

# Generate 1000 data points between -3 and 3
x = np.linspace(-3, 3, 1000)

# Calculate the corresponding y-values for the Normal Distribution
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

# Create the plot
plt.plot(x, y, label=f'μ={mu}, σ={sigma}')
plt.title('Normal Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)

# Save the plot as an image
plt.savefig('normal_distribution_plot.png')
print("Plot saved as 'normal_distribution_plot.png'")
