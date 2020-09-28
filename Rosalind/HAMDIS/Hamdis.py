from itertools import product

f = open('rosalind_ba1g.txt')
lines=[]
raw = f.readlines()
f.close()
for each in raw:
    lines.append(each.rstrip())

k = int(lines[0].rstrip())
lines = lines[1:]

kmers = []

for each in lines:
    tupadd = []
    for i in range(len(each) - k + 1):
        toadd = each[i:i+k]
        tupadd.append(toadd)
    kmers.append(tupadd)
    
def HamDis(s, q):
    dis = 0
    for i in range(len(s)):
        if s[i] != q[i]:
            dis += 1
            
    return dis



realkmers = product(["A","G","C","T"], repeat = k)
rkmers = []
for each in realkmers:
    s = ""
    for car in each:
        s+= car
    rkmers.append(s)
    
    
curmin = 0
minkmer = ""

for kmer in rkmers:
    runtotal = 0
    for line in kmers:
        for ktext in line:
            #print(kmer,ktext + " " +str(HamDis(kmer, ktext)))
            runtotal += HamDis(kmer, ktext)
            
        if curmin == 0:    
            curmin = runtotal
            minkmer = kmer
        else:
            if runtotal <= curmin:
                curmin = runtotal
                minkmer = kmer
            
#===============================================================================
# 
# for line in kmers:
#     for kmer in line:
#         runtotal = 0
#         for sec in rkmers:
#                 runtotal += HamDis(kmer, sec)
#             
#         if curmin == 0:    
#             curmin = runtotal
#         else:
#             if runtotal < curmin:
#                 curmin = runtotal
#                 minkmer = kmer
#                 
#===============================================================================
print(kmers)
print(rkmers)
print(curmin)
print(minkmer)  
