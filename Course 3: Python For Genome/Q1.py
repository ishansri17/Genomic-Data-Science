import sys
f = open('dna2.fasta', 'r')
file = f.read()
print(file.count('>'))