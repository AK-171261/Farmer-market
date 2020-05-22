import unittest
import farmer_market


class Testfarmer_market(unittest.TestCase):

    def test_FarmerMarket(self):
        self.assertEqual(farmer_market.farmer_market(['CF1', 'CF1', 'CF1', 'AP1']), 22.84)
        self.assertEqual(farmer_market.farmer_market(['CH1', 'AP1', 'AP1', 'AP1', 'MK1']), 16.61)
        self.assertEqual(farmer_market.farmer_market(['CH1', 'AP1']), 9.11)
        self.assertEqual(farmer_market.farmer_market(['CH1', 'AP1', 'CF1', 'MK1']), 20.34)
        self.assertEqual(farmer_market.farmer_market(['MK1', 'AP1']), 10.75)
        self.assertEqual(farmer_market.farmer_market(["AP1", "AP1", "CH1", "AP1"]), 16.61)
        self.assertEqual(farmer_market.farmer_market(['CF1', 'CF1']), 11.23)
        self.assertEqual(farmer_market.farmer_market(["AP1", 'OM1', "OM1"]), 10.38)


if __name__ == '__main__':
    unittest.main()
