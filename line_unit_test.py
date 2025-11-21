import unittest
from line_fitting_pipeline import generate_synthetic_data, fit_line_from_csv

class TestLineFittingPipeline(unittest.TestCase):
    def test_fit_line_accuracy(self):
        # Set true slope and intercept values
        m_true, b_true = 2.5, 1.0
        filename = "test_synthetic_data.csv"
        # Generate synthetic data with known parameters
        generate_synthetic_data(m=m_true, b=b_true, filename=filename)
        # Load data and fit a line to it
        _, _, m_fit, b_fit = fit_line_from_csv(filename=filename)
        # Assert fitted slope is close to true slope within tolerance
        self.assertAlmostEqual(m_fit, m_true, delta=0.2)
        # Assert fitted intercept is close to true intercept within tolerance
        self.assertAlmostEqual(b_fit, b_true, delta=0.5)
        # Print fitted values for verification
        print(m_fit , b_fit)

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
