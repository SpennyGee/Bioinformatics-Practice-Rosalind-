from Bio import SeqIO

f = SeqIO.parse('rosalind_edit.txt', 'fasta')
raw = []
for each in f:
    raw.append(str(each.seq))


s = raw[0]
q = raw[1]

len_s = len(s)
len_q = len(q)

if len_s >= len_q:
    longer = s
    shorter = q
else:
    longer = q
    shorter = s
    
def edit_dis(a, b):
    
    n = len(a)
    m = len(b)
    
    edit_matrix =[[0 for x in range(n+1)] for y in range(m+1)]


    for i in range(n+1):
        edit_matrix[0][i] = i
    for j in range(m+1):
        edit_matrix[j][0] = j


    for i in range(1, len(edit_matrix)):
        for j in range(1, len(edit_matrix[0])):
      
            if a[j - 1] == b[i-1]:
                edit_matrix[i][j] = edit_matrix[i-1][j-1]
                
            else:

                cv1 = edit_matrix[i-1][j-1]
               
                cv2 = edit_matrix[i][j-1]
                
                cv3 = edit_matrix[i-1][j]
               
                to_consider = [cv1,cv2,cv3]
                
                edit_matrix[i][j]= min(to_consider) + 1
             
    return(edit_matrix[m][n])


a = "PRETTY"
b = "PRETTEIN"

f = open('rosalind_ba1g.txt', 'r')
r = list(f.readlines())
    
s = r[0]
q = r[1]
f.close()
print(edit_dis(a, b))
#print(HamDis(s, q))

#===============================================================================
# Console Friendly version:
# 
# def edit_dis(a, b):
#     
#     n = len(a)
#     m = len(b)
#     
#     edit_matrix =[[0 for x in range(n+1)] for y in range(m+1)]
# 
# 
#     for i in range(n+1):
#         edit_matrix[0][i] = i
#     for j in range(m+1):
#         edit_matrix[j][0] = j
# 
# 
#     for i in range(1, len(edit_matrix)):
#         for j in range(1, len(edit_matrix[0])):
#       
#             if a[j - 1] == b[i-1]:
#                 edit_matrix[i][j] = edit_matrix[i-1][j-1]
#         
#             else:
# 
#                 cv1 = edit_matrix[i-1][j-1]
#                
#                 cv2 = edit_matrix[i][j-1]
#                 
#                 cv3 = edit_matrix[i-1][j]
#                
#                 to_consider = [cv1,cv2,cv3]
#                 
#                 edit_matrix[i][j]= min(to_consider) + 1
#     
#     print("        ", end = "")
#     for i in range(len(a)):
#         print(a[i], end = "  ")
#     print()
#     
#     j = 0
#     while j < len(b) + 1:
#         if j > 0:
#             print(b[j - 1], end = "   ")
#         else:
#             print("    ", end ="")
#         print(edit_matrix[j])
#         j += 1
#     print()
#     return(edit_matrix[m][n])
# 
# def HamDis(s, q):
#     dis = 0
#     s_len = len(s)
#     q_len = len(q)
#     if s_len >= q_len:
#         longer = s
#         shorter = q
#     else:
#         longer = q
#         shorter = s
#      
#     for i in range(len(longer)):
#         if i < len(shorter):
#             if s[i] != q[i]:
#                 dis += 1
#         else:
#             dis += 1
#     return dis
# 
# a = "PRETTY"
# b = "PRETTEIN"
# 
# print(edit_dis(b, a))
# 
#     
# f = open('rosalind_ba1g.txt', 'r')
# r = list(f.readlines())
#     
# s = r[0]
# q = r[1]
# f.close()
#===============================================================================


