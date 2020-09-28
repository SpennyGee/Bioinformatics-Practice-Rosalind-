# want to determine minimum number of reversals required to transform one permutation
# to another of the same length. Easiest to create an inverse transformation of the two
# sequences and then transform that to the identity sequence 



# creates an inverse permutation of a sequence...
# original sequence acts as a map for an inverse permutation where
# the current index represents the future value to go in a new
# list indexed by current values...ie [1,8,9,3,2,7,6,5,4,10] would map
# 2 to the 8th index of a new list (3 to 9th place, 4 to 3rd place, etc.)
# resulting in [1, 5, 4, 9, 8, 7, 6, 2, 3, 10]
def invperm(t):
    # o is identity sequence (1,2,3,....,n)
    o = []
    for i in range(len(t)):
        o.append(i+1)
    
    r = [0 for x in range(len(t))]

    for i in range(len(t)):
        
       
        r[t[i] - 1] = o[i]

    return r
#print(invperm([1,8,9,3,2,7,6,5,4,10]))

# similar approach to above where one list acts as a map for the other
# the values of the list in first argument act as a map. So the value in index 0 of list 1
# is used as the index to get the value from list 2, which are then places in a new list in order...
# so list 1 = [3, 1, 2] and list 2 = [1,3,2], then we return r =[2, 1, 3]

def twoinv(t, o):
    r = [0 for x in range(len(o))]

    for i in range(len(o)):
        pos = t[i] - 1
        val = o[pos]
        r[i] = val
        #print(r)
    return r

# This single list returned by twoinv() is all we need! Just have to perform operations/reversals on this list
# and transform it to the identity permutation. The same operations could then be performed on list 1 to transform it to list 2 :)

def bps_used(seq1, seq2):
    bpts_used = []
    i = 0
    while seq1[i] == seq2[i]:
        i += 1
    bpts_used.append(int(i+1))
    i += 1
    while i < len(seq1):
        if seq1[i:] != seq2[i:]:
            i += 1
            
        else:
            bpts_used.append(int(i))
            break
    if len(bpts_used) < 2:
        bpts_used.append(len(seq1))
    
    return bpts_used
        
        

# performs single reversal on a list between two breakpoints (inclusive)
def revpoints(l, b1, b2):
    #print("reversal between indicies (" + str(b1) + ", " +str(b2) + ")")
    s = []
    sub1 = l[:b1]
    torev = l[b1:b2]
    sub2 = l[b2:]

    torev = torev[::-1]
    
    for each in sub1:
        s.append(each)
    for each in torev:
        s.append(each)
    for each in sub2:
        s.append(each)
    #print(s)
    return s
        
# determines break points (locates numbers out of place from identity sequence)
def place_breaks(l):
    
    bps = []
    if l[0] != 1:
        bps.append(0)
        
    for i in range(len(l) - 1):
        p = l[i]
        n = l[i+1]
        if abs(p - n) != 1:
            bps.append(i+1)
    if l[len(l)-1] != (len(l) + 1):
        bps.append(len(l) + 1)
    return bps
    
# Need to transform A into identity vector (1,2,3,...n)
bp = []

# input block = goal is to take two perms and make them into two lists using regular expressions

#===============================================================================
# in_one = input("Please enter the first permutation: ")
# in_two = input("Please enter the second permutation: ")
# # Try to use regexp to just get the digits from any input! so, just like, r'[\d]+' should just get digits and ignore punctuation or spaces?
# for each_one, each_two in in_one, in_two:
#     perm_one = in_
#===============================================================================

A = twoinv([6,1,5,4,3,2], invperm([6,4,3,1,5,2]))
print("From the two original permutations, we create a map, A: ", end = "")
print(A,)
print("that we want to transform into the identity permutation by a serires of reversals.")
print("The operations (reversals between certain breakpoints) done to our map correspond")
print("exactly to those required to transform permumation 1 into permutation 2.")
print()

#print()
seq = []
seq.append(A)
# considers every reversal sequence that ress between
# all possible break points and choices those with the least
# remaining breakpoints to proceed
# (note break points can only be reduced by 0, 1 or 2 with any reversal)


# List to store number of reversals in a particualr sequence of reversals
# Minimum of this list will be our result. 
Q = []

#pass a list, the breakpoints of a list, and the number of reversals
# that list has already undergone...can we Pass along the old/prev list
# to trace back best path??
FinalSeqs = []
def check_revs(seq, breaks, count):

    
    A = seq[-1]
    #print("last seq...")
    #print(A)
    #we're done! A is the identity matrix
    if breaks == 1:
        Q.append(count)
        FinalSeqs.append(seq)
        print("starting at ", end = "")
        print(seq[0])
        print("the next sequence and the indicies of reversal points are...")
        for i in range(len(seq) - 1):
            prev_seq = seq[i]
            next_seq = seq[i+1]
            bpts_used = bps_used(prev_seq, next_seq)
            print(next_seq, end = " ")
            print(bpts_used)
        
            
##        #print(min(Q))
##        print("the sequence consisting of...")
##        
##        for each in seq:
##            print(each)
        print("This series was completed in ", end = "")
        print(count, end = " ")
        print("steps.")
        print()
    # A is not the identity matrix and we need to check all possible
    # reversals of A, then proceed from that set of reversals with the
    # sequences with the fewest remaining breakpoints
        
    else:

        #list of all breakpoints in A
        bps = place_breaks(A)

        # a list of all possible reversals between  all breakpoints
        allbreaks = []

        # go over all possible reversals bettwen two breakpoints
        # and add them to allbreaks
        for i in range(len(bps) - 1):
            for j in range(1, len(bps)):
                
                
                b1 = bps[i]
                b2 = bps[j]
                if abs(b1 - b2) > 1 and b2 > b1:
                    allbreaks.append(revpoints(A, b1, b2))
                
        # a list to hold the best reversals, those with the fewest breakpoints
        bestrevs = []

        # original amout of breakpoints from A...
        # a given reversal can have either the same number
        # of breakpoints, or exactly one or two fewer.
        cmin = len(bps)

        # find minimum number of breakpoints in allbreaks
        for each in allbreaks:
            checkbp = place_breaks(each)
            cur = len(checkbp)
            if cur < cmin:
                cmin = cur
        # add any reversal from all breaks with the min
        # number of breakpoints to bestrevs.
        for each in allbreaks:
            checkbp = place_breaks(each)
            cur = len(checkbp)
            if cur == cmin:
                bestrevs.append(each)

        # pass along best rev to check_revs to continue, incresing count       
        for each in bestrevs:
            new_seq = []
            for prev_seq in seq:
                new_seq.append(prev_seq)
            new_seq.append(each)
            check_revs(new_seq, len(place_breaks(each)), count+1)
            
            

((check_revs(seq, len(place_breaks(A)), 0)))
print("So the minimum number of reversals required to turn our map into the identity matrix is ", end = "")
print(min(Q))
print()
##print("breakpoints used to get from [1, 4, 5, 9, 8, 7, 6, 2, 3, 10] to [1, 4, 5, 3, 2, 6, 7, 8, 9, 10]:")
##print(bps_used([1, 4, 5, 9, 8, 7, 6, 2, 3, 10], [1, 4, 5, 3, 2, 6, 7, 8, 9, 10]))

# now update to keep track of particular operations on a given sequence and return fewest
# probably not efficient but can we create a dictionare where its a sequence as key and value
# is the reversals (def by breakpoints)

#ideas for improvements...make a list of all completed sequences of reversals, then, once completed, find min and just return one seqeunce from that list of minimum length
# also, check against current minimum of Q...if a sequence of reversals is being considered, make sure it is equal to or less than min count
# before further processing