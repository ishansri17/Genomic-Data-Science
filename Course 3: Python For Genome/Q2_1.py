import sys
f = open('dna2.fasta', 'r')
file = f.read()
#print(file.count('>'))

dictLen = {}

from Bio import SeqIO

for seq in SeqIO.parse('dna2.fasta', 'fasta'):
    if seq.id not in dictLen:
        dictLen[seq.id] = len(seq.seq)

maxVal = max(dictLen.values())
minVal = min(dictLen.values())
maxes = []
mins = []

for key in dictLen.keys():
    if dictLen[key] == maxVal:
        maxes.append(key)
    if dictLen[key] == minVal:
        mins.append(key)

print("Length of the sequences are: " + ', '.join(str(x) for x in dictLen.values()))
print("Longest sequence length is: " + str(maxVal))
print("Shortest sequence length is: " + str(minVal))
print("ID's of longest sequences are: " + ', '.join(str(x) for x in maxes))
print("ID's of shortest sequences are: " + ' '.join(str(x) for x in mins))