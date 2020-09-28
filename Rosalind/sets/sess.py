from Bio import SeqIO


f = SeqIO.parse('rosalind_cat.txt','fasta')
line =  []
for each in f:
    line.append(each.seq)
seq = line[0]

def solve(rna):
    """
    An input RNA consisting of {A, U, C, G}
    The number of non-overlapping perfect 
    matchings.
    """
    return helper(rna, 0, len(rna) - 1, {})


def helper(rna, lo, hi, dp):
    
    mapping = {
    "A" : "U",
    "U" : "A",
    "G" : "C",
    "C" : "G"
    }
    characters = hi - lo + 1
    
    # if there are an odd number of nucleotides, 
    # this is an invalid matching.
    if characters % 2 == 1:
        return 0

    # handles tricky edge cases.
    if lo >= hi or lo >= len(rna) or hi < 0:
        return 1

    # return answer if it is memoized.    
    if (lo, hi) in dp:
        return dp[(lo, hi)]
    else:
        curr = rna[lo]
        target = mapping[curr]
        acc = 0
        for i in range(lo + 1, hi + 1, 2):
            if rna[i] == target:
                left = helper(rna, lo + 1, i - 1, dp)
                right = helper(rna, i + 1, hi, dp)
                acc += (left * right) % 1000000
        dp[(lo, hi)] = acc
        return acc


rna = "CAUAUG"

print(solve(seq) % 1000000)