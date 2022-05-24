#Input given sequence
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
#Define a variable called fragment with an initial value of 0
fragment=0
#Count the number of enzyme digestion sites
a=seq.count("GAATTC")
#The number of fragments is equal to the number of sites plus 1
fragment = a + 1
print(fragment)
#In conclusion, if we use the EcoRI enzyme to cut this sequence, the total number of fragments is 1.Because there is no EcoRI enzyme site in this sequence.
