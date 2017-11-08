import random
GENES = ['A', 'T', 'C', 'G']
PAIRS_MAPPING = {'A':'T', 'T': 'A', 'C':'G', 'G': 'C'}

def createPairGenes(length):
    gene1 = ''
    gene2 = ''
    for i in range (length):
        randomIndex = random.randint(0, len(GENES) - 1)
        gene1 += GENES[randomIndex]
        gene2 += PAIRS_MAPPING[gene1[i]]

    print (gene1)
    print (gene2)
    print (gene2[::-1])

def pair_genes_forward(s1, s2):
    if len(s1) != len(s2):
        return False

    if len(s1) + len(s2) == 0:
        return True

    if PAIRS_MAPPING[s1[0]] == s2[0]:
        return pair_genes(s1[1:], s2[1:])
    else:
        return False

def pair_genes_backward(s1, s2):
    if len(s1) != len(s2):
        return False

    if len(s1) + len(s2) == 0:
        return True

    if PAIRS_MAPPING[s1[0]] == s2[-1]:
        return pair_genes(s1[1:], s2[:-1])
    else:
        return False

def pair_genes(s1, s2):
    return pair_genes_forward(s1,s2) or pair_genes_backward(s1, s2)

def zip_length(s):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 0
    else:
        if PAIRS_MAPPING[s[0]] == s[-1]:
            return 1 + zip_length(s[1:-1])
        else:
            return 0
if __name__ == "__main__":
    createPairGenes(7)
    print(zip_length('AATCATGCAGCTGCATGATT'))
