import sys
f = open('dna2.fasta', 'r')
file = f.read()
print(file.count('>'))

from Bio import SeqIO
list1 = []
for filename in SeqIO.parse('dna2.fasta', 'fasta'):
    list1.append((filename.id, str(filename.seq), len(filename)))
    print(len(filename))