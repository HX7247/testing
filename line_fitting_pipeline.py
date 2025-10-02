import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_synthetic_data(m=2.5, b=1.0, num_points=100, x_range=(0, 10), noise_std=2.0, filename="synthetic_data.csv"):
    np.random.seed(42)
    X = np.linspace(x_range[0], x_range[1], num_points)
    noise = np.random.normal(0, noise_std, num_points)
    Y = m * X + b + noise
    df = pd.DataFrame({'X': X, 'Y': Y})
    df.to_csv(filename, index=False)
    return X, Y, m, b

def fit_line_from_csv(filename="synthetic_data.csv"):
    df = pd.read_csv(filename)
    X = df['X'].values
    Y = df['Y'].values
    m_fit, b_fit = np.polyfit(X, Y, 1)
    return X, Y, m_fit, b_fit

def plot_results(X, Y, m_true, b_true, m_fit, b_fit, filename="fit_plot.png"):
    plt.figure(figsize=(8, 6))
    plt.scatter(X, Y, label="Data", color="blue", alpha=0.5)
    plt.plot(X, m_true * X + b_true, label="Original Line", color="green", linestyle="--")
    plt.plot(X, m_fit * X + b_fit, label="Best Fit Line", color="red")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.title("Line Fitting: Original vs Best Fit")
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    X, Y, m_true, b_true = generate_synthetic_data()
    X_loaded, Y_loaded, m_fit, b_fit = fit_line_from_csv()

    plot_results(X_loaded, Y_loaded, m_true, b_true, m_fit, b_fit)
