import unittest
from a1 import *

class TestPairGenes(unittest.TestCase):
    def test_empty_pairs(self):
        gene1 = ''
        gene2 = ''
        expected = True
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "2 empty pairs of genes should match!")

    def test_basic_pairs1(self):
        gene1 = 'A'
        gene2 = 'T'
        expected = True
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "A and T should match!")

    def test_basic_pairs2(self):
        gene1 = 'C'
        gene2 = 'G'
        expected = True
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "C and G should match!")

    def test_combination_pairs(self):
        gene1 = 'TGTACCACGTAGCTA'
        gene2 = 'ACATGGTGCATCGAT'
        expected = True
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "combinations of AT and CG should match!")

    def test_combination_pairs_reverse(self):
        gene1 = 'TGTACCACGTAGCTA'
        gene2 = 'TAGCTACGTGGTACA'
        expected = True
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "combinations of AT and CG should match!")

    def test_combination_pairs_long(self):
        gene1 = 'GTCATGAGCTTTTGACAAGACCCCTTTGCTGCGGGATCCCGCTAAAAGATATAGCCCAGAGAAGTAGCTCGCGTCCGCTGCGGTTACGCGGCAATCCGCG'
        gene2 = 'CAGTACTCGAAAACTGTTCTGGGGAAACGACGCCCTAGGGCGATTTTCTATATCGGGTCTCTTCATCGAGCGCAGGCGACGCCAATGCGCCGTTAGGCGC'
        expected = True
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "combinations of AT and CG should match!")

    def test_combination_pairs_long_reverse(self):
        gene1 = 'GTCATGAGCTTTTGACAAGACCCCTTTGCTGCGGGATCCCGCTAAAAGATATAGCCCAGAGAAGTAGCTCGCGTCCGCTGCGGTTACGCGGCAATCCGCG'
        gene2 = 'CGCGGATTGCCGCGTAACCGCAGCGGACGCGAGCTACTTCTCTGGGCTATATCTTTTAGCGGGATCCCGCAGCAAAGGGGTCTTGTCAAAAGCTCATGAC'
        expected = True
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "combinations of AT and CG should match!")

    def test_compare_self(self):
        gene1 = 'AATCATGCAGCTGCATGATT'
        gene2 = 'TTAGTACGTCGACGTACTAA'
        expected = True
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "gene1 == gene2, and they are pair genes")

    def test_basic_pairs1(self):
        gene1 = 'A'
        gene2 = 'C'
        expected = False
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "A and C should not match!")

    def test_basic_pairs2(self):
        gene1 = 'C'
        gene2 = 'T'
        expected = False
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "C and T should not match!")

    def test_almost_similar(self):
        gene1 = 'GTCATGAGCTTTTGACAAGACCCCTTTGCTGCGGGATCCCGCTAAAAGATATAGCCCAGAGAAGTAGCTCGCGTCCGCTGCGGTTACGCGGCAATCCGCG'
        gene2 = 'CAGTACTCGAAAACTGTTCTGGGGAAACGACGCCCTAGGGCGATTTTCTATATCGGGTCTCTTCATCGAGCGCAGGCGACGCCAATGCGCCGTTAGGCGT'
        expected = False
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "Last nucleotide do not match")

    def test_different_length(self):
        gene1 = 'GTTGACTGATTACACCCAC'
        gene2 = 'CAACTGACTAATGTGGGTGC'
        expected = False
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "Genes having different lengths should fail!")

    def test_compare_self(self):
        gene1 = 'GTTGACTGATTACACCCACG'
        gene2 = 'GTTGACTGATTACACCCACG'
        expected = False
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "gene1 == gene2, but they arent pairs")


class TestZipLength(unittest.TestCase):

    def test_empty_gene(self):
        gene = ''
        expected = 0
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "empty string should have 0 pairs")

    def test_single_length(self):
        gene = 'A'
        expected = 0
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "string of length 1 cannot really zip")

    def test_basic_pairs(self):
        gene = 'AT'
        expected = 1
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "AT is 1 Match")

    def test_basic_pairs(self):
        gene = 'GC'
        expected = 1
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "GC is 1 Match")

    def test_no_pairs(self):
        gene = 'GTATCATGGT'
        expected = 0
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "No pairs whatsoever!")

    def test_no_outer_pair(self):
        gene = 'CTAACCCAAT'
        expected = 0
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "Middle of the gene pairs while the ends of gene does not pair")

    def test_do_pair(self):
        gene = 'AATCATGCAGCTGCATGATT'
        expected = 10
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "Pairs!")

    def test_do_pair_long(self):
        gene = 'TACGCACTGTGAGTAAGATGCGGCTCCACACTTGTTAGAAGCTCAATAAATTTATTGAGCTTCTAACAAGTGTGGAGCCGCATCTTACTCACAGTGCGTA'
        expected = 50
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "Pairs!")

    def test_do_not_pair_all_1(self):
        gene = 'AGTAGCGTATGTACGCTACT'
        expected = 9
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "Do not pair all the way!")

    def test_do_not_pair_all_2(self):
        gene = 'GTTTTAGGTACCTCAAAC'
        expected = 4
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "Do not pair all the way!")

    def test_do_not_pair_all_3(self):
        gene = 'GCGCTCACGGTCTACTAGACCGTGAGCGC'
        expected = 14
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "Odd lengthed string can only pair up to the char before the middle one")

    def test_backward_forward_do_not_pair(self):
        gene = 'ACCATGAAGTACCA'
        expected = 0
        actual = zip_length(gene)
        self.assertEqual(expected, actual, "Palindromes do not pair")

if __name__ == "__main__":
    unittest.main(exit=False)
