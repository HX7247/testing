import unittest
from line_fitting_pipeline import generate_synthetic_data, fit_line_from_csv

class TestLineFittingPipeline(unittest.TestCase):
    def test_fit_line_accuracy(self):
        # Set known parameters
        m_true, b_true = 2.5, 1.0
        filename = "test_synthetic_data.csv"
        # Generate synthetic data
        generate_synthetic_data(m=m_true, b=b_true, filename=filename)
        # Fit line to the data
        _, _, m_fit, b_fit = fit_line_from_csv(filename=filename)
        # Assert fitted values are close to true values within a tolerance
        self.assertAlmostEqual(m_fit, m_true, delta=0.2)
        self.assertAlmostEqual(b_fit, b_true, delta=0.5)

if __name__ == "__main__":
    unittest.main()
