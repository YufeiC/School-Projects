import unittest
from testdata import *


class TestPairGenes(unittest.TestCase):
    def test_empty_pairs(self):
        gene1 = ''
        gene2 = ''
        expected = True
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "2 empty pairs of genes should match!")

    def test_basic_pairs_1(self):
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

    def test_basic_pairs_3(self):
        gene1 = 'A'
        gene2 = 'C'
        expected = False
        actual = pair_genes(gene1, gene2)
        self.assertEqual(expected, actual, "A and C should not match!")

    def test_basic_pairs_4(self):
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

    def test_compare_self_2(self):
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

    def test_basic_pairs_2(self):
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

class TestMatchMask(unittest.TestCase):

    def test_empty_both(self):
        gene = ''
        mask = ''
        expected = -1
        actual = match_mask(gene, mask)
        self.assertEqual(expected, actual, "empty gene and empty mask have nothing to match")

    def test_obvious_no_match(self):
        gene = 'AC'
        mask = '***'
        expected = -1
        actual = match_mask(gene, mask)
        self.assertEqual(expected, actual, "Length of mask < gene not possible")

    def test_basic_mask(self):
        gene = 'ATCGT'
        mask = 'TAGC*'
        expected = 0
        actual = match_mask(gene, mask)
        self.assertEqual(expected, actual, "Basic pairing with star")

    def test_basic_mask_2(self):
        gene = 'ATCGT'
        mask = '*CGAT'
        expected = 0
        actual = match_mask(gene, mask)
        self.assertEqual(expected, actual, "Basic pairing backwards with star")

    def test_basic_mask_3(self):
        gene = 'A'
        mask = '*'
        expected = 0
        actual = match_mask(gene, mask)
        self.assertEqual(expected, actual, "* matches any nucleotide")

    def test_no_match(self):
        gene = 'AGCT'
        mask = '**A*'
        expected = -1
        actual = match_mask(gene, mask)
        self.assertEqual(expected, actual, "No match in either direction")

    def test_multiple_match_forward(self):
        gene = 'GTATA'
        mask = '*AT'
        expected = 0
        actual = match_mask(gene, mask)
        self.assertEqual(expected, actual, "Multiple matches choose first (forward)")

    def test_multiple_match_backward(self):
        gene = 'GTATA' #'ATATG'
        mask = 'TA*'
        expected = 0
        actual = match_mask(gene, mask)
        self.assertEqual(expected, actual, "Multiple matches choose first (backward)")

    def test_multiple_forward_and_backward(self):
        gene = 'GTATA' #'ATATG'
        mask = 'TA*'
        expected = 0
        actual = match_mask(gene, mask)
        self.assertEqual(expected, actual, "Multiple matches choose first (backward)")

    def test_brackets(self):
        gene = 'GTAGA'
        mask = 'T[GA]*'
        expected = 0
        actual = match_mask(gene, mask)
        self.assertEqual(expected, actual, "brackets")

    def test_numbers(self):
        gene = 'GACTATA'
        mask = '*3AT'
        expected = 0
        actual = match_mask(gene, mask)
        self.assertEqual(expected, actual, "numbers")


class TestSpliceGene(unittest.TestCase):

    def test_no_change(self):
        gene1 = list('AT')
        gene2 = list('TA')
        anchor1 = 'A'
        anchor2 = 'T'
        splice_gene(gene1, gene2, anchor1, anchor2)
        self.assertEqual(gene1, gene1)
        self.assertEqual(gene2, gene2)

    def test_basic(self):
        gene1 = list('AGT')
        gene2 = list('ACT')
        anchor1 = 'A'
        anchor2 = 'T'
        splice_gene(gene1, gene2, anchor1, anchor2)
        self.assertEqual(gene1, [])
        self.assertEqual(gene2, gene1)

    def test_basic_backwards(self):
        gene1 = list('TGA')
        gene2 = list('ACT')
        anchor1 = 'A'
        anchor2 = 'T'
        splice_gene(gene1, gene2, anchor1, anchor2)
        self.assertEqual(gene1, [])
        self.assertEqual(gene2, list('AGT'))

if __name__ == "__main__":
    unittest.main(exit=False)
