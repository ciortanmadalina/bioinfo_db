import random

def createRandomString(n):
    random.seed(7)
    seq = ''.join([random.choice('ACGT') for _ in range(10)])
    print('string : ' + seq)
    return seq
def longestCommonPrefix(s1, s2):
    i = 0
    while 1< len(s1) and i< len(s2) and s1[i] == s2[i]:
        i+=1
    return s1[:i]

basePairs = {'A' : 'T', 'C' : 'G', 'G' :'C', 'T' : 'A'}

def reverseComplement(s):
    t = ''
    for base in s:
        t = basePairs[base] + t
    return t

def complement(s):
    t = ''
    for base in s:
        t = t + basePairs[base]
    return t
#https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/lambda_virus.fa

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
        return genome


def baseFrequency():
    genome = readGenome('lambda_virus.fa')
    counts = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
    for base in genome:
        counts[base] += 1
import collections
print(collections.Counter(readGenome('lambda_virus.fa')))

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            q = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(q)
    return sequences, qualities

def phred33ToQ(qual):
    return ord(qual)-33

def createHist(qualities):
    hist = [0] * 50
    for qual in qualities:
        for pfred in qual:
            q = phred33ToQ(pfred)
            hist[q] += 1
    return hist

print(complement(createRandomString(10)))
print(readGenome('lambda_virus.fa')[:100])
