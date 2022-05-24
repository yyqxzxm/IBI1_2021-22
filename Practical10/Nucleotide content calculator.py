#input a sequence
DNA = input('please input a DNA sequence:')
#define a function
def percentage(DNA):
#Set four variables
    a = DNA.count('A')
    t = DNA.count('T')
    c = DNA.count('C')
    g = DNA.count('G')
#Calculate the ratio of each type of base to the total number of bases
    S = a + t + c + g
    A=a/S
    T=t/S
    C=c/S
    G=g/S
    print("The percentage of base A is %f"%A)
    print("The percentage of base T is %f"%T)
    print("The percentage of base C is %f"%C)
    print("The percentage of base G is %f"%G)
#run the function
percentage(DNA)
