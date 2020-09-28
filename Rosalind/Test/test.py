from Bio import SeqIO
#from test.test_contains import seq
#from Bio.Seq import translate

def factorial(n):
    if n == 1 or n == 0 :
        return 1
    else:
        return (n*factorial(n-1))
   
        

def split(word): 
    return [char for char in word]  
      
f = SeqIO.read("rosalind_pmch.txt", "fasta")

seq = f.seq
#print(seq)

#print()
AUcount = 0
total = len(seq)
strseq = str(seq)
lisseq = split(strseq)
##print(lisseq)
for char in lisseq:
    if char == 'A':
        AUcount +=1
GCcount = int((total - AUcount*2)/2)
print(GCcount)
##print(AUcount)
#print(factorial(GCcount)*factorial(AUcount))
        










#===============================================================================
# 
# 
# o = o_seq[0]
# introns = o_seq[1:]
# 
# fin = str(o.seq)
# 
# print(fin)
# print()
# for each in introns:
#     
#     check = str(each.seq)
#     print(check)
#     fin = fin.replace(check, "")
# 
# print() 
# 
# print(translate(fin))
#===============================================================================

