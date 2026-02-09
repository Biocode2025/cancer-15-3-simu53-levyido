import random


file=open('data/data.txt','r')
file2=open('data/codontab.txt','r')
file3=open('results/results.txt','w')
dna = ""


for line in file:
  line=line.strip()
  line = line.upper()
  if line.startswith('>'):
    continue
  else:
    dna+=line

for line in file2:
  line=line.strip()
  line = line.upper()
 


mutation=random.randrange(1,101)
if mutation==100:
  mutation="add"
elif mutation==99:
  mutation="remove"
else:
  mutation="switch"
if mutation=="add" or mutation=="remove":
   mutnum=random.randrange(1,4)

mutplace=random.randrange(0,len(dna))

codon=random.randrange(1,5)
if codon==1:
  codon="A"
if codon==2:
  codon="T"
if codon==3:
  codon="C"
if codon==4:
  codon="G"





if mutation=="switch":
  dna = dna[:mutplace] + codon + dna[mutplace+1:]
if mutation=="add":
 dna = dna[:mutplace] + codon * mutnum + dna[mutplace:]
if mutation=="remove":
 dna = dna[:mutplace] + dna[mutplace+mutnum:]

file3.write(dna)
 
