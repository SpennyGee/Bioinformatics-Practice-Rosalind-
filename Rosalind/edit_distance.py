from Bio import SeqIO
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
#===============================================================================
# print("       P  L  E  A  S  A  N  T  L  Y")
# i = 0
# for each in edit_matrix:
#     if i == 0:
#         print(end = "   ")
#     if i > 0:
#         print(b[i - 1], end = "  ")
#     
#     print(each)
#     i += 1
#===============================================================================
print("The edit distance is " , end = "")
print(edit_matrix[m][n], end = ".")
    
f = SeqIO.parse('rosalind_edit.txt', 'fasta')
raw = []
for each in f:
    raw.append(str(each.seq))


a = raw[0]
b = raw[1]

n = len(a)
m = len(b)
edit_matrix = L =[[0 for x in range(n+1)] for y in range(m+1)]


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
             
            
#===============================================================================
# print("       P  L  E  A  S  A  N  T  L  Y")
# i = 0
# for each in edit_matrix:
#     if i == 0:
#         print(end = "   ")
#     if i > 0:
#         print(b[i - 1], end = "  ")
#     
#     print(each)
#     i += 1
#===============================================================================
print("The edit distance is " , end = "")
print(edit_matrix[m][n], end = ".")
        
