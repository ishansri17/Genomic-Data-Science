import sys
from Bio import SeqIO

f = open('dna2.fasta', 'r')
file = f.read()

dictSeq = {}
start_codon = ['ATG']
stop_codon = ['TAA', 'TAG', 'TGA']
dictORF = {}
dictORFPos = {}

frame = int(input("Enter a frame to read ORF's (Either 1, 2, or 3): "))
if frame < 1 or frame > 3:
    print('Please enter a valid frame.')
    sys.exit(1)

for seq in SeqIO.parse('dna2.fasta', 'fasta'):
    if seq.id not in dictSeq:
        dictSeq[seq.id] = seq.seq

for id in dictSeq.keys():
    currORF = ''
    orf = False
    startPos = 0
    orfList = []
    # iterate through sequence for each id
    for i in range(frame-1, len(dictSeq[id]), 3):
        # if the current codon is a start codon, we add it to our ORF and set the boolean to true
        if dictSeq[id][i:i+3] in start_codon:
            orf = True
            currORF = currORF + dictSeq[id][i:i+3]
            startPos = i+1
        # if the current codon is a stop codon, we finalize our ORF, add it to the dict, and make the boolean false
        elif dictSeq[id][i:i+3] in stop_codon:
            if orf:
                orf = False
                currORF = currORF + dictSeq[id][i:i + 3]
                orfList.append(currORF)
                dictORF[id] = orfList
                dictORFPos[currORF] = startPos
        # if its not a start or a stop codon, only if it is in the ORF, we add it to the current string
        else:
            if orf:
                currORF = currORF + dictSeq[id][i:i+3]

maxVal = 0
maxID = []
for key in dictORF.keys():
    currMax = max(dictORF[key], key=len)
    length = len(currMax)
    if length > maxVal:
        maxVal = length
        maxID.append(key)


print("The longest ORF has a length of: " + str(maxVal))
print("The ID of the sequence containing the longest ORF is: " + str(maxID))
print("These are the each ID's with their longest ORF and its starting positions: ")
for id in dictORF.keys():
    maxORF = max(dictORF[id], key=len)
    length = len(maxORF)
    start = dictORFPos[maxORF]
    print("\tID:\t\t\t" + str(id) + "\n\tLength:\t\t" + str(length) + "\n\tSequence:\t" + str(maxORF) + "\n\tPosition:\t" + str(start) + "\n")