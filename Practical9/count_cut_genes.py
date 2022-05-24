import re
new_filename=input('in put a new filename:')#read the file
output=open(new_filename,'w')#output the results
ccc=open("cut_genes.fa") 
w=ccc.read()
w=w+">"
w=re.sub(r"\n","",w)
seq=re.findall(r' (.+?)>',w)

n=re.findall(r'>(.+?) ',w)  
length=len(n)

ns=[]
for h in range(length):
    ns.append(n[h])

print(length)

pieces=[]
for h in seq:
    cut=i.find('GAATTC')
    piece=cut+2
    pieces.append(fragment)
print(len(pieces))

for h in range(length):
    output.write(">")
    output.write(ns[h])
    output.write(" ")
    output.write(str(pieces[h]))
    output.write("\n")
    output.write(seq[h])
    output.write("\n")
output.close()
# you can verify that this output file contains the name of the gene,the number of cuts made in this gene by EcoRI and the DNA sequence in the correct FASTA format.

