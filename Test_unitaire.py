import unittest
import fonction_test

class TestAddition(unittest.TestCase):
    def test_addition_positives(self):
        self.assertEqual(fonction_test.addition(2, 3), 5)  #Test 2 positifs

    def test_addition_negatives(self):
        self.assertEqual(fonction_test.addition(-2, -3), -5)  #Test 2 négatifs

    def test_addition_mix(self):
        self.assertEqual(fonction_test.addition(2, -3), -1)  #Test positif + négatif

    def test_addition_virgules(self):
        self.assertEqual(fonction_test.addition(2.5, 3.1), 5.6)  #Test nombres à virgule


if __name__ == "__main__":
    unittest.main()