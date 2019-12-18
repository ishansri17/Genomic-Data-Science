import sys
from Bio import SeqIO

file = open('dna2.fasta', 'r')
f = file.read()

dictCount = {}

seqList = []
for line in SeqIO.parse('dna2.fasta', 'fasta'):
    seqList.append(line.seq)

length = int(input("Please enter a length 'n': "))
if length < 1:
    print("Please enter a valid length")
    sys.exit(1)

for seq in seqList:
    for i in range(0, len(seq), 1):
        if seq[i:i+length] not in dictCount:
            dictCount[seq[i:i+length]] = 0

fullSeq = ''.join(str(seq) for seq in seqList)

for i in range(0, len(fullSeq), 1):
    segment = fullSeq[i:i+length]
    if segment in dictCount.keys():
        dictCount[segment] += 1

for segment in dictCount.keys():
    if dictCount[segment] > 1:
        print(segment + ": " + str(dictCount[segment]))

max_count = max(dictCount.values())
max_segment = max(dictCount, key=dictCount.get)

print("The most frequent sequence was " + str(max_segment) + " with a count of " + str(max_count) + ".")

