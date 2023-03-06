#program to practice unit testing, data from 'surfshop.py'

import surfshop
import unittest
import datetime

class SurfShopTest(unittest.TestCase):
  
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboard(self):
    argument = 1
    function = self.cart.add_surfboards(argument)
    expected = f'Successfully added {argument} surfboard to cart!'

    self.assertEquals(function, expected, f"Expected {function} to equal {expected}")

  def test_add_multiple_surfboards(self):
    argument = [2, 3, 4]
    for num in argument:
      with self.subTest(num):
        self.setUp()
        function = self.cart.add_surfboards(num)
        expected = f"Successfully added {num} surfboards to cart!"

        self.assertEquals(function, expected, f"Expected {function} to equal {expected}")

  @unittest.skip("Off Season")
  def test_too_many_surfboards(self):
    argument = 5
    expected = surfshop.TooManyBoardsError

    self.assertRaises(expected, self.cart.add_surfboards, argument)
  
  # @unittest.skip("Feature in development")
  def test_apply_locals_discount(self):
    self.assertTrue(self.cart.apply_locals_discount())
  
  @unittest.skip("WIP")
  def test_set_checkout_date(self):
      argument = datetime.datetime.now
      self.cart.set_checkout_date(argument)
      self.assertEquals(self.checkout_date, argument, f"Expected {self.checkout_date} to equal {argument}")

unittest.main()