import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_synthetic_data(m=2.5, b=1.0, num_points=100, x_range=(0, 10), noise_std=2.0, filename="synthetic_data.csv"):
    """Generate synthetic linear data with noise and save to CSV."""
    np.random.seed(42)  # Set seed for reproducibility
    X = np.linspace(x_range[0], x_range[1], num_points)  # Create evenly spaced X values
    noise = np.random.normal(0, noise_std, num_points)  # Generate random noise
    Y = m * X + b + noise  # Calculate Y values with noise
    df = pd.DataFrame({'X': X, 'Y': Y})  # Create DataFrame
    df.to_csv(filename, index=False)  # Save to CSV file
    return X, Y, m, b

def fit_line_from_csv(filename="synthetic_data.csv"):
    """Load data from CSV and fit a line to it."""
    df = pd.read_csv(filename)  # Read CSV file
    X = df['X'].values  # Extract X values
    Y = df['Y'].values  # Extract Y values
    m_fit, b_fit = np.polyfit(X, Y, 1)  # Fit line and get slope and intercept
    return X, Y, m_fit, b_fit

def plot_results(X, Y, m_true, b_true, m_fit, b_fit, filename="synthetic_plot.png"):
    """Plot original data, original line, and best-fit line."""
    plt.figure(figsize=(8, 6))  # Create figure
    plt.scatter(X, Y, label="Data", color="blue", alpha=0.5)  # Plot data points
    plt.plot(X, m_true * X + b_true, label="Original Line", color="green", linestyle="--")  # Plot original line
    plt.plot(X, m_fit * X + b_fit, label="Best Fit Line", color="red")  # Plot fitted line
    plt.xlabel("X-Axis")  # Label X axis
    plt.ylabel("Y-Axis")  # Label Y axis
    plt.legend()  # Add legend
    plt.title("Line Fitting: Original vs Best Fit")  # Add title
    plt.savefig(filename)  # Save plot to file
    plt.close()  # Close plot

if __name__ == "__main__":
    # Generate synthetic data
    X, Y, m_true, b_true = generate_synthetic_data()
    # Load data and fit line
    X_loaded, Y_loaded, m_fit, b_fit = fit_line_from_csv()
    # Plot and save results
    plot_results(X_loaded, Y_loaded, m_true, b_true, m_fit, b_fit)
