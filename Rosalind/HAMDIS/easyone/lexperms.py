import itertools

f = open('rosalind_lexv1.txt', 'r')
raw = f.readlines()
seq = raw[0].rstrip('\n')
n = raw[1].rstrip('\n')

s = []
for each in seq:
    s.append(each)

    

print(seq)
print(n)

r=s

allem = []
x = int(n) + 1
for i in range(1, int(x)):
    
    p = itertools.product(r, repeat = i)
    
    for each in p:
    
        fmt = ""
        for y in each:
            if y != ' ':
                fmt += y
            if fmt not in allem:
                allem.append(fmt)
allem.remove('')
print()

srt_perm = sorted(allem,
                  key=lambda word: [seq.index(c) for c in word])
with open('answer3.txt', 'a') as f:
    for j in srt_perm:
        f.write('%s\n' % j)
        print(j)
        
        
