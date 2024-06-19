import unittest
import pandas as pd
from unittest.mock import patch
from io import StringIO

# Assuming the code above is in a function called `quantity_check` in a module called `quantity_check`
from quantity_check import quantity_check

class TestQuantityCheck(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Building_block_ID': ['BB1', 'BB2', 'BB3'],
            'Frequency': [1, 2, 3],
            'Molecular_weight': [100, 200, 300],
            'Quantity_in_stock': [120, 240, 360]
        })

    @patch('builtins.input', side_effect=['120'])
    def test_scale_validation(self, mock_input):
        self.assertEqual(quantity_check(self.df), 120)

    def test_quantity_calculation(self):
        self.df['Quantity_needed'] = self.df['Frequency'] * 120 * self.df['Molecular_weight']*(10^-6)+0.5*(100*10^-6)*self.df['Molecular_weight']
        self.assertTrue((self.df['Quantity_needed'] == [120, 240, 360]).all())

    def test_enough_quantity(self):
        self.df['Enough_quantity'] = self.df['Quantity_needed'] <= self.df['Quantity_in_stock']
        self.assertTrue((self.df['Enough_quantity'] == [True, True, True]).all())

    def test_low_stock_blocks(self):
        low_stock_blocks = self.df.loc[self.df['Enough_quantity'] == False, 'Building_block_ID']
        self.assertTrue(low_stock_blocks.empty)

if __name__ == '__main__':
    unittest.main()