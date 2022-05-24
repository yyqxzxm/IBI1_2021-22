import re
##read original file
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
#Output the results in a new fasta file cut_genes.fa
final = open('cut_genes.fa','w')

seq=[] 
row=[]
DNA=[]
pathway=[]
m = file.read()
m = re.sub(r"\n","",m)
m = m +">"

genes=re.findall(r'](.+?)>',m)
names=re.findall(r'gene:(.+?) gene',m)  


ett = 0
# find the name of the gene
for m in genes:
    if m.find('GAATTC')>=0:
        row.append(ett)
        seq.append(m)
#put the gene name into  the sequence
    ett = ett + 1

for m in row:
    DNA.append(DNA[m])

for i in seq:
    length=len(m)
    pathway.append(length)

for i in range(len(row)):
    final.write(">")
    final.write(DNA[m])
    final.write(" ")
    final.write(str(pathway[m]))
    final.write("\n")
    final.write(seq[m])
    final.write("\n")
final.close()
#you can check that the script can read the original fasta file and create a new file cut_genes.fa with sequences of genes that contain sequences that can be cut by EcoRI.
