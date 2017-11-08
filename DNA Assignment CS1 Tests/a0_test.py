import unittest
from a0 import *

class TestSplitInput(unittest.TestCase):

    def test_empty_string(self):
        s = ''
        expected = ['', '', '']
        actual = split_input(s)
        self.assertEqual(expected, actual, "Empty string split")

    def test_only_up_stream(self):
        s = 'ATCGGCTCATCGATTTGG'
        expected = ['ATCGGCTCATCGATTTGG', '', '']
        actual = split_input(s)
        self.assertEqual(expected, actual, "Only up stream")

    def test_no_down_stream(self):
        s = 'ATCGGCTCATCGATGTGG'
        expected = ['ATCGGCTCATCG', 'ATGTGG', '']
        actual = split_input(s)
        self.assertEqual(expected, actual, "No down stream")

    def test_everything(self):
        s = 'ATCGGCTCATCGATGTGGATGYYYATGZZZ'
        expected = ['ATCGGCTCATCG', 'ATGTGG', 'ATGYYYATGZZZ']
        actual = split_input(s)
        self.assertEqual(expected, actual, "Missing or incorrectly produced some streams of data")

    def test_everything_invalid_gene(self):
        s = 'ATCGGCTCATCGATGTGGAATGYYYATGZZZ'
        expected = ['ATCGGCTCATCG', 'ATGTGGA', 'ATGYYYATGZZZ']
        actual = split_input(s)
        self.assertEqual(expected, actual, "Missing or incorrectly produced some streams of data")

    def test_no_upstream(self):
        s = 'ATGATGATGATGATGATG'
        expected = ['', 'ATG', 'ATGATGATGATGATG']
        actual = split_input(s)
        self.assertEqual(expected, actual, "No up stream")


class TestGetGene(unittest.TestCase):

    def test_empty_string(self):
        s = ''
        expected = "Error"
        actual = get_gene(s)
        self.assertEqual(expected, actual, "Empty string error")

    def test_only_up_stream(self):
        s = 'ATCGGCTCATCGATTTGG'
        expected = "Error"
        actual = get_gene(s)
        self.assertEqual(expected, actual, "Only up stream")

    def test_no_down_stream(self):
        s = 'ATCGGCTCATCGATGTGG'
        expected = "ATGTGG"
        actual = get_gene(s)
        self.assertEqual(expected, actual, "No down stream")

    def test_everything(self):
        s = 'ATCGGCTCATCGATGTGGATGYYYATGZZZ'
        expected = 'ATGTGG'
        actual = get_gene(s)
        self.assertEqual(expected, actual, "Invalid gene")

    def test_everything_invalid_gene(self):
        s = 'ATCGGCTCATCGATGTGGAATGYYYATGZZZ'
        expected = 'ATGTGGA'
        actual = get_gene(s)
        self.assertEqual(expected, actual, "Invalid gene in the middle of the string")

    def test_no_upstream(self):
        s = 'ATGATGATGATGATGATG'
        expected = 'ATG'
        actual = get_gene(s)
        self.assertEqual(expected, actual, "Multiple ATG genes")

class TestValidateGene(unittest.TestCase):

    def test_empty_string(self):
        s = ''
        expected = False
        actual = validate_gene(s)
        self.assertEqual(expected, actual, "Empty string isn't valid")

if __name__ == "__main__":
    unittest.main(exit=False)
