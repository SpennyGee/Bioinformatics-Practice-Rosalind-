
f = open('rosalind_eval.txt', 'r')
raw = []
for each in  f.readlines():
    raw.append(each.rstrip('\n'))
print(raw)

n = raw[0]
seq = raw[1]
B = raw[2].split(' ')

b = [float(each) for each in B]
print(b[1] + b[2])

NumOfPossibleEvents = int(n) - len(seq) + 1
res = []
ATc = 0
GCc = 0
for j in range(len(seq)):
    print(seq[j])
    if seq[j] == 'A' or seq[j] == 'T':
        ATc += 1
        print("why")
    elif seq[j] == 'G' or seq[j] == 'C':
        GCc += 1
print(ATc)
print(GCc)
for i in range(len(b)):
    pGC = b[i]
    pAT = (1 - pGC) / 2
    pGC = pGC/ 2
    
   
    print
    pSeq = (pGC ** GCc) * (pAT ** ATc)
    r = pSeq * (NumOfPossibleEvents)
    g = float("{0:.3}".format(r))
    res.append(g)

for each in res:
    print(each, end = " ")        
    
            
    