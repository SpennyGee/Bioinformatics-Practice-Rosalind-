# Want to find shortest superstring of a collection of strings...
#
# Organize the strings into a list, and duplicate that list into temp_list
#
# inspect temp and find the strings with the most overlap...
# combine those into one string and add to temp, deleting the originals 
# repeat until the length of temp is one. 
    
def count_overlap(a,b):
    
    all_overlaps = []
    
    if len(a) >= len(b):
        longer = a 
        shorter = b 
    else:
        longer = b 
        shorter = a 
    print(longer)
    print(shorter)
    # check  overlap count at each possible overlay of shorter on longer, for example,
    # aaaaa   aaaaa    aaaaa   aaaaa     aaaaa     and     aaaaa      aaaaa
    # bbb      bbb       bbb      bbb        bbb          bbb       bbb
    #
    # note the overlap count can be at most len(shorter)
    print()
    # check pre-total overlap...
    for i in range(len(longer) - len(shorter)):
        sub_longer = longer[:i+1]
        sub_shorter = shorter[-1*(i+1):]
        
        print(sub_longer)
        print(sub_shorter)
        overlap = 0
         
        for j in range(len(sub_shorter)):
             
            l_char = sub_longer[j]
            s_char = sub_shorter[j]
             
            if l_char == s_char:
                overlap += 1
        
        print(overlap)
        all_overlaps.append(overlap)
    deduction = 1
    for i in range(len(longer)):
        if i <= len(longer) - len(shorter):
            
        # inspect each substring of longer of len(shorter)
            sub_longer = longer[i:len(shorter)+i]
            sub_shorter = shorter
            print(sub_longer)
            print(sub_shorter)
        
        else:
            
            sub_longer = longer[i:len(shorter)+ i - deduction]
            sub_shorter = shorter[:-1*deduction]
            print(sub_longer)
            print(sub_shorter)
            deduction = deduction + 1
            
            
        overlap = 0
         
        for j in range(len(sub_shorter)):
             
            l_char = sub_longer[j]
            s_char = sub_shorter[j]
             
            if l_char == s_char:
                overlap += 1
        
        print(overlap)
        all_overlaps.append(overlap)
    print()
    return(max(all_overlaps))
    
print(count_overlap('dsfj', 'seiotjng'))

def overlap(a, b):
   
    if len(a) >= len(b):
        longer = a 
        shorter = b 
    else:
        longer = b 
        shorter = a
        
    max_overlap = count_overlap(a, b)
    
    for i in range(len(longer) - len(shorter)):
        sub_longer = longer[:i+1]
        sub_shorter = shorter[-1*(i+1):]
        
        print(sub_longer)
        print(sub_shorter)
        overlap = 0
         
        for j in range(len(sub_shorter)):
             
            l_char = sub_longer[j]
            s_char = sub_shorter[j]
             
            if l_char == s_char:
                overlap += 1
        
        if overlap  == max_overlap:
            
        all_overlaps.append(overlap)
    deduction = 1
    for i in range(len(longer)):
        if i <= len(longer) - len(shorter):
            
        # inspect each substring of longer of len(shorter)
            sub_longer = longer[i:len(shorter)+i]
            sub_shorter = shorter
            print(sub_longer)
            print(sub_shorter)
        
        else:
            
            sub_longer = longer[i:len(shorter)+ i - deduction]
            sub_shorter = shorter[:-1*deduction]
            print(sub_longer)
            print(sub_shorter)
            deduction = deduction + 1
            
            
        overlap = 0
         
        for j in range(len(sub_shorter)):
             
            l_char = sub_longer[j]
            s_char = sub_shorter[j]
             
            if l_char == s_char:
                overlap += 1
        
        print(overlap)
        all_overlaps.append(overlap)