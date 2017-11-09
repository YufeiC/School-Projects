import random
GENES = ['A', 'T', 'C', 'G']
PAIRS_MAPPING = {'A':'T', 'T': 'A', 'C':'G', 'G': 'C', '*': 'ATCG'}

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

def match_mask(gene, mask):
    '''
    (str, str) -> int
    '''

    denumbered_mask = denumberfy_mask(mask)

    gene_size = len(gene)
    mask_size = len(denumbered_mask)
    mask = denumbered_mask
    gene_index = 0
    mask_index = 0
    match_index = -1

    while (gene_index < gene_size and mask_index < mask_size):

        # if it's a left bracket
        if mask[mask_index] == '[':
            # find right bracket and then match
            right_bracket_index = mask.index(']', mask_index)
            # find the string between the brackets
            nucleotides_to_check = mask[mask_index + 1: right_bracket_index]
        # otherwise it's simply a nucleotide
        else:
            right_bracket_index = mask_index # no such thing
            nucleotides_to_check = mask[mask_index]

        do_match = match_nucleotide(gene[gene_index], nucleotides_to_check)
        # if the nucleotide or nucleotides match with that part of the mask
        if do_match:
            # set match_index to only the first time it matches
            if match_index == -1 and mask_index == 0:
                match_index = gene_index
            mask_index = right_bracket_index + 1
        else:
            mask_index = 0
            match_index = -1

        # increment the gene index only
        gene_index += 1

    # if there were still
    if mask_index < mask_size or gene_index < gene_size :
        match_index = -1

    return match_index

def denumberfy_mask(mask):
    new_mask = ''

    size = len(mask)
    index = 0

    while (index < size):
        # if the character is a number
        if (mask[index].isdigit()):
            new_mask += (mask[index - 1] * (int(mask[index]) - 1))
        else:
            new_mask += mask[index]
        index += 1

    return new_mask

def match_nucleotide(nucleotide, sub_mask):
    '''
    (char, char or [options] or *) -> bool
    '''
    do_match = False
    size = len(sub_mask)
    index = 0

    while(index < size and not do_match):
        do_match = (nucleotide in PAIRS_MAPPING[sub_mask[index]])
        index += 1

    return do_match


if __name__ == "__main__":
    #createPairGenes(7)
    #print(zip_length('AATCATGCAGCTGCATGATT'))
    print(match_mask("TGGGG", "[AG]C3*"))
