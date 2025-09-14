# My First Project

This project demonstrates a fundamental probability concept: the **Normal Distribution**.

## What does this code do?
- It uses the `numpy` library to generate data points.
- It calculates the probability density for the Normal Distribution using its formula.
- It uses the `matplotlib` library to plot the famous Gaussian bell curve.
- It saves the plot as an image file.

## The Math Behind It
The formula for the probability density function of the Normal Distribution is:

$$
f(x | \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

Where:
- $\mu$ is the mean
- $\sigma$ is the standard deviation

## How to Run This Code
1. Make sure you have Python installed.
2. Install the required libraries: `pip install numpy matplotlib`
3. Run the script: `python normal_distribution.py`
4. It will create a file called `normal_distribution_plot.png`.
