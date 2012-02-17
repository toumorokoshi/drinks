"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import Drinks.utils as utils
import unittest


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class TestUtils(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_toSlug(self):
        cases = {'Vodka Cran (NEHI)':'vodkacran'}
        for case in cases.keys():
            self.assertEqual(utils.toSlug(case),cases[case])
