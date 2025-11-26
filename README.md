# Line Fitting Pipeline - README

## Overview
This repository contains a small pipeline to:
- generate synthetic linear data with noise,
- fit a best-fit line to the data,
- plot the original and fitted lines,
- and run unit tests validating the fitted slope and intercept.

## Files
- line_fitting_pipeline.py — functions:
  - generate_synthetic_data(m, b, num_points, x_range, noise_std, filename)
  - fit_line_from_csv(filename)
  - plot_results(X, Y, m_true, b_true, m_fit, b_fit, filename)
- line_unit_test.py — unit test for the pipeline.
- unit_test.py — simple unit tests for addition/subtraction helpers.
- test_function.py — sample functions used by `unit_test.py`.

## Requirements
- Python 3.8+
- numpy
- pandas
- matplotlib

Install dependencies (Windows):
```powershell
python -m pip install numpy pandas matplotlib
```

## Usage
1. Generate data, fit, and save plot:
```powershell
python line_fitting_pipeline.py
```
This creates `synthetic_data.csv` and `synthetic_plot.png`.

2. Run the unit tests:
- Run a specific test file:
```powershell
python line_unit_test.py
```
- Or run all tests with unittest discover:
```powershell
python -m unittest discover -v
```

## Tests and tolerances
The unit test `line_unit_test.py` generates a small test CSV and asserts the fitted slope/intercept are close to the true values. Tolerances used in the test are:
- slope (m): delta=0.2
- intercept (b): delta=0.5

## Notes
- The random seed in `generate_synthetic_data` is fixed for reproducibility.
- If you want less deterministic behavior, remove or change the seed.
- Plots are saved to the working directory; open the PNG file to inspect results.