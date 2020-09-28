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
    
    print("        ", end = "")
    for i in range(len(a)):
        print(a[i], end = "  ")
    print()
     
    j = 0
    while j < len(b) + 1:
        if j > 0:
            print(b[j - 1], end = "   ")
        else:
            print("    ", end ="")
        print(edit_matrix[j])
        j += 1
    print()
    return(edit_matrix)
#===============================================================================
# 
# a = "PRETTY"
# b = "PRTTEIN"
# 
# edit_dis(b, a)
#===============================================================================

    
f = open('rosalind_ba1g.txt', 'r')
r = list(f.readlines())
    
s = r[0]
q = r[1]
f.close()

# okay, to rebuild best alignment sequence, start at index (m,n) == final spot. 
# we will end up with two optimal alignment sequences, a0 and b0, each having the same length. 
# so we have an index for each original string, a and b, to keep track of where we're at
# in bringing those characters to the alignment sequences.
# if the letters are the same at the current index, add that character to the current index
# in each of a0 and b0 and move diagonally to the next step in the matrix. 
# if the two characters being evaluated are not the same, we are to chose the best/minimum
# from the alignment matrix from am[i-1][j-2], am[i-1][j], am[i][j-1]. 
# if the minimum is up, we add b[i]0 = b[i] and a[j] = '-' and we set indicies to new spot (stays on a0 and goes to b[i-1]0)
# if minimum  is left, we print add b0 = '-' and a[j] = a[j]0, move index accordingly (stays on b0 and goes to a[j-1]0)
# if minimum is diagonal, a[j]0 = a[j] and b[i]0 = b[i] and move to a[j-1]b[i-1]
#
# to get out/base case...
# i = 0 j = 0...

# a takes string for top of matrix
# b takes string for side of matrix
# we want longer on top for consistency.

def align_seq(a, b):
    
    row = len(a)
    col = len(b)
    
    if row >= col:
        longer = len(a) 
        shorter =len(b)
        alignment_matrix = edit_dis(a, b)
    else:
        longer = len(b)
        shorter = len(a)
        alignment_matrix = edit_dis(b, a)
    
            
    cur_val = alignment_matrix[shorter][longer]
            
    cur_char_a = a[longer - 1]
    cur_char_b = b[shorter - 1]
    
    if len(a) == 1 and len(b) == 1:
        print("a = " + cur_char_a)
      
    else:
        
            # need to check left, up and diagonal up/left, find min, and move in that direction,
            # adding characters appropriately (char or -)
            # 
       
            cv1 = alignment_matrix[shorter-1][longer-1]
           
            cv2 = alignment_matrix[shorter][longer-1]
            
            cv3 = alignment_matrix[shorter-1][longer]
           
            neighbor_min = min([cv1,cv2,cv3])
            
            # move left
            if cv2 == neighbor_min:
                
                align_seq(a[:-1], b)
                print(cur_char_a, end = "")
                print("-", end= "")
                
            #diagonal min
            if cv1 == neighbor_min:
                align_seq(a[:-1],b[:-1])
                print(cur_char_a, end = "")
                print(cur_char_b, end="")  
            
            
            
            # move up
            elif cv3 == neighbor_min:
                align_seq(a, b[:-1])
                print('-', end = "")
                print(cur_char_b, end = "")
                
                
         

align_seq("pleasantly", "meanly")