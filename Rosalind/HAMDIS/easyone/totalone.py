#===============================================================================
# f = open('rosalind_ba10a.txt')
# raw = f.readlines()
# lines = []
# use = []
# for each in raw:
#     lines.append(each)
# print(lines[6])
# use.append(lines[0].rstrip())
# use.append(lines[5].rstrip())
# use.append(lines[6].rstrip())
# print(use[2])
# path = use[0]
# use[1] = str(use[1]).replace("A\t", "")
# use[1] = str(use[1]).replace("\t", " ")
# use[2] = str(use[2]).replace("B\t", "")
# use[2] = str(use[2]).replace("\t", " ")
# use[1] = str(use[1]).split(" ")
# use[2] = str(use[2]).split(" ")
# print(use)
# AA = use[1][0]
# AA = float(str(AA).replace("'", ""))
# 
# AB = use[1][1]
# AB = float(str(AB).replace("'", ""))
# 
# BA = use[2][0]
# BA = float(str(BA).replace("'", ""))
# 
# BB = use[2][1]
# BB = float(str(BB).replace("'", ""))
# 
# 
# 
# 
# probs = {
#     "A" : [AA, AB],
#     "B" : [BA, BB]
#     }
# 
# 
# prob = .5
# 
# for i in range(1, len(path)):
#     prev = path[i-1]
#     curr = path[i]
#     pt = probs[prev]
#     pa = pt[0]
#     pb = pt[1]
#     if curr == "A":
#         prob = prob * pa
#     else:
#         prob = prob * pb
# print(prob)
#===============================================================================
#===============================================================================
# 
# f = open('rosalind_ba10b.txt')
# raw = f.readlines()
# lines = []
# use = []
# for each in raw:
#     lines.append(each)
# print(lines)
# use.append(lines[0].rstrip())
# use.append(lines[4].rstrip())
# use.append(lines[9].rstrip())
# use.append(lines[10].rstrip())
# print(use)
# path = use[1]
# use[2] = str(use[2]).replace("A\t", "")
# use[2] = str(use[2]).replace("\t", " ")
# use[3] = str(use[3]).replace("B\t", "")
# use[3] = str(use[3]).replace("\t", " ")
# use[2] = str(use[2]).split(" ")
# use[3] = str(use[3]).split(" ")
# print(use)
# AX = use[2][0]
# AX = float(str(AX).replace("'", ""))
# AY = use[2][1]
# AY = float(str(AY).replace("'", ""))
# AZ = use[2][2]
# AZ = float(str(AZ).replace("'", ""))
# 
# BX = use[3][0]
# BX = float(str(BX).replace("'", ""))
# BY = use[3][1]
# BY = float(str(BY).replace("'", ""))
# BZ = use[3][2]
# BZ = float(str(BZ).replace("'", ""))
# 
# 
# 
# act = use[0]
# 
# probs = {
#     "A" : [AX, AY, AZ],
#     "B" : [BX, BY, BZ]
#     }
# 
# print(AX)
# 
# prob = 1
# 
# for i in range(0, len(path)):
#     curr = path[i]
#     real = act[i]
#     pt = probs[curr]
#     px = pt[0]
#     py = pt[1]
#     pz = pt[2]
#     
#     if real == 'x':
#         prob = prob * px
#     if real == 'y':
#         prob = prob * py
#     if real == 'z':
#         prob = prob * pz
# print(prob)
#===============================================================================
#===============================================================================
# from _operator import index
#===============================================================================
#===============================================================================
# 
# f = open('rosalind_ba10c.txt')
# raw = f.readlines()
# lines = []
# use = []
# for each in raw:
#     lines.append(each)
# print(lines)
# use.append(lines[0].rstrip())
# use.append(lines[7].rstrip())
# use.append(lines[8].rstrip())
# use.append(lines[9].rstrip())
# use.append(lines[12].rstrip())
# use.append(lines[13].rstrip())
# use.append(lines[14].rstrip())
# print(use)
# path = use[0]
# use[1] = str(use[1]).replace("A\t", "")
# use[1] = str(use[1]).replace("\t", " ")
# use[2] = str(use[2]).replace("B\t", "")
# use[2] = str(use[2]).replace("\t", " ")
# use[3] = str(use[3]).replace("C\t", "")
# use[3] = str(use[3]).replace("\t", " ")
# use[1] = str(use[1]).split(" ")
# use[2] = str(use[2]).split(" ")
# use[3] = str(use[3]).split(" ")
#  
# use[4] = str(use[4]).replace("A\t", "")
# use[4] = str(use[4]).replace("\t", " ")
# use[5] = str(use[5]).replace("B\t", "")
# use[5] = str(use[5]).replace("\t", " ")
# use[6] = str(use[6]).replace("C\t", "")
# use[6] = str(use[6]).replace("\t", " ")
# use[4] = str(use[4]).split(" ")
# use[5] = str(use[5]).split(" ")
# use[6] = str(use[6]).split(" ")
# print(use)
# AX = use[1][0]
# AX = float(str(AX).replace("'", ""))
# AY = use[2][0]
# AY = float(str(AY).replace("'", ""))
# AZ = use[3][0]
# AZ = float(str(AZ).replace("'", ""))
#  
# BX = use[1][1]
# BX = float(str(BX).replace("'", ""))
# BY = use[2][1]
# BY = float(str(BY).replace("'", ""))
# BZ = use[3][1]
# BZ = float(str(BZ).replace("'", ""))
#  
#  
# CX = use[1][2]
# CX = float(str(CX).replace("'", ""))
# CY = use[2][2]
# CY = float(str(CY).replace("'", ""))
# CZ = use[3][2]
# CZ = float(str(CZ).replace("'", ""))
#  
#  
#  
# act = use[0]
#  
#  
# xs = [AX, AY, AZ]
# ys = [BX, BY, BZ]
# zs = [CX, CY, CZ]
# a = [xs, ys, zs]
#  
#      
# def maxlist(l):
#     ma = 0
#     index = 0
#     mindex = 0
#     for each in l:
#         if each > ma:
#             print(each)
#             ma = each
#             mindex = index
#         index += 1
#     return mindex
#  
# xn = maxlist(xs)
# yn = maxlist(ys)
# zn = maxlist(zs)
# ns = [xn, yn, zn]
# lets = []
# for each in ns:
#     if each == 0:
#         lets.append("A")
#     if each == 1:
#         lets.append("B")
#     if each == 2:
#         lets.append("C")
# print(lets)
# print(maxlist(xs))
# prob = 1
#  
# s = ""
# print(path)
# for i in range(0, len(path)):
#      
#     real = act[i]
#     if real == 'x':
#         s+= lets[0]
#     if real == 'y':
#         s+= lets[1]
#     if real == 'z':
#         s+= lets[2]
# print(s)
#      
#===============================================================================
x = "zxxxxyzzxyxyxyzxzzxzzzyzzxxxzxxyyyzxyxzyxyxyzyyyyzzyyyyzzxzxzyzzzzyxzxxxyxxxxyyzyyzyyyxzzzzyzxyzzyyy"
transition = [[0.634, 0.366], [0.387, 0.613]]
emission = [[0.532, 0.226, 0.241], [0.457, 0.192, 0.351]]
state = []

for j in range(len(transition)):  
    toadd = []
      
    for i in range(len(x)):
        pos = 0
        slet = x[i]
        if slet == 'y':
            pos = 1
        if slet =='z':
            pos = 2
        toadd.append(emission[j][pos])
    state.append(toadd)

def maxInCol(l, col):
    curmax = 0
    for i in range(len(l)):
        check = l[i][col]
        if check >= curmax:
            curmax = check
            
    return curmax
Row = ['A', 'B']

for i in range(len(transition)):
    
    state[i][0] = state[i][0] * maxInCol(transition, i)

for i in range(1, len(x)):
    for j in range(len(transition)):
        state[j][i] = state[j][i] * maxInCol(state, i - 1)
for each in state:
    print(each)
path = ""
for i in range(len(x)):
    cmax = 0
    letr = ""
    for j in range(len(Row)):
        if state[j][i] > cmax:
            cmax = state[j][i]
            letr = Row[j]
    path += letr
print(path)
            
        
    













        
