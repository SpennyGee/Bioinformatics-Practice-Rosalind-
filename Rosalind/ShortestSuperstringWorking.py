from Bio import SeqIO


f = SeqIO.parse('rosalind_long.txt', 'fasta')
seq = []
for each in f:
    seq.append(str(each.seq))

a = ["abc", "bca","dab", 'aaa','atx','zbt']
#a = seq
def longer_string(a,b):
    #returns longer of a and b
    if len(a) >= len(b):
        return a 
    else:
        return b 
    
def shorter_string(a,b):

    #returns shorter of a and b
    if len(a) < len(b):
        return a 
    else:
        return b
    
def count_overlap(s1, s2):
    # determines maximum overlapping chars between two strings
    max_overlap = 0
    long = longer_string(s1, s2)
    short = shorter_string(s1, s2)
   
    # check prefixes of long against suffixes of short
    for i in range(len(short)):
        short_suffix = short[-1 *(i+1):]
        long_prefix = long[:i+1]
     
        
        if short_suffix == long_prefix:
            overlap = i+1
            if overlap > max_overlap:
                max_overlap = overlap
    #check prefixes of short against suffixes of long
    for i in range(len(short)):
        short_prefix = short[:i+1]
        long_suffix =  long[-1*(i+1):]
        
        if short_prefix == long_suffix:
            overlap = i+1
            if overlap > max_overlap:
                max_overlap = overlap
    
    return(max_overlap)

def combine(s1, s2):
    # combines two strings to the shortest superstring - if there is no overlap, returns s1+s2
    max_overlap = count_overlap(s1, s2)
    long = longer_string(s1, s2)
    short = shorter_string(s1, s2)
    res = ""
    for i in range(len(short)):
        short_suffix = short[-1 *(i+1):]
        long_prefix = long[:i+1]
        short_rest = short[:-1 *(i+1)]
        long_rest = long[(i+1):]
       
        if short_suffix == long_prefix and (i+1 == max_overlap):
            res = short_rest + short_suffix + long_rest
    for i in range(len(short)):
        short_prefix = short[:i+1]
        long_suffix =  long[-1*(i+1):]
        short_rest = short[(i+1):]
        long_rest = long[:-1 *(i+1)]
       
        if short_prefix == long_suffix and (i+1 == max_overlap):
            res = long_rest + long_suffix + short_rest
        if res == "":
            res = s1 + s2
    return(res)
 
# go through list twice. First iteration finds most overlapping characters between any two strings.
# the second iteration then finds two strings in the list whose overlap is equal to the max overlap.
# combine these two max overlapping strings into a new string (using overlapping section only once)
# and delete two original strings. Repeat until list only has one string.

while len(a) > 1:
    max_overlap = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                overlap = count_overlap(a[i], a[j])
                if overlap > max_overlap:
                    max_overlap = overlap
                   
    for i in range(len(a)):
        for j in range(len(a)):
            
            
            if i != j:
                max_found = False
                overlap = count_overlap(a[i], a[j])
                if overlap == max_overlap and max_found == False:
                    to_remove = [a[i], a[j]]
                    
                    max_found = True
   
    remove1 = to_remove[0]
  
    remove2 = to_remove[1]
    add = combine(remove1,remove2)  
    a.remove(remove1)
    a.remove(remove2)
    a.append(add)
    
print(a[0])

                
                
