import copy
from Bio import SeqIO
print("test, first result from new keyboard!")
def longer_string(a,b):
    #returns longer of a and b
    if len(a) >= len(b):
        return a 
    else:
        return b 
def shorter_string(a,b):

    #returns shorter of a and b
    if len(a) <= len(b):
        return a 
    else:
        return b
class Overlap:
    def __init__(self, short, prcnt):
        self.res = short
        self.percent = prcnt
    
def count_overlap(s1, s2):
    
    shortest = s1+s2
    potentialshortest = ""
    maxoverlap = 0
    
    for i in range(len(s1) + 1):
        sub1 = s1[-1*i:]
        rest1 = s1[:-1*i]
        sub2 = s2[:i]
        rest2 = s2[-1*len(s2)+i:]
     
        if(sub1 == sub2):
            if (len(sub1) > maxoverlap):
                maxoverlap = len(sub1)
                potentialshortest = rest1 + sub1 + rest2
            if len(potentialshortest) < len(shortest):
                if potentialshortest != "":
                    shortest = potentialshortest
            potentialshortest = ""
    
    for j in range(1, len(s2)):
        sub1 = s1[:-1*j]
        p = -1 * len(s2) + j
        sub2 = s2[p:]
        rest1 = s1[-1*j:]
        rest2 = s2[:j]
       
        if(sub1 == sub2):
            if len(sub1) > maxoverlap:
                maxoverlap = len(sub1)
                potentialshortest = rest2 + sub1 + rest1
            if len(potentialshortest) < len(shortest):
                if potentialshortest != "":
                
                    shortest = potentialshortest
            potentialshortest = ""
        
    
    print(s1)
    print(s2)
    print(shortest)
    print()
    overlap_percent = len(shortest) / (len(s1) + len(s2))
    
    return(Overlap(shortest, overlap_percent))
    
a = count_overlap("2test", "test1")

print(a.res)
print(a.percent)

f = SeqIO.parse('rosalind_long.txt', 'fasta')
to_check = []
for each in f:
    to_check.append(str(each.seq))

temp = copy.deepcopy(to_check)

res = []
for i in range(len(temp) - 1):
    for j in range(i+1,len(temp)):
        if i != j:
            
            to_add = count_overlap(temp[i], temp[j])
            res.append(to_add)

q = (([x.percent for x in res]))
print(min(q))

for i in range(len(temp) - 1):
    for j in range(i+1,len(temp)):
        if i != j:
            to_check = count_overlap(temp[i], temp[j])
            if to_check.percent == min(q):
                del temp[i]
                del temp[j]
                temp.append(to_check)
