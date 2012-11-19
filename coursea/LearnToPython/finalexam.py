def double_last(L):
    L[-1]*=2

def get_nag_nonnag(L):
    nonneg=[]
    neg=[]
    for row in range(len(L)):
        for col in range(len(L)):
            if L[row][col]<0:
                neg.append(L[row][col])
            elif L[row][col]>=0:
                nonneg.append(L[row][col])

    return (neg,nonneg)

#print(get_nag_nonnag([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]]))

def add_to_counts(d,s):
    for c in s:
        d[c]+=1

        
def swap_words(two_words):
    first=two_words[:two_words.find(' ')]
    second=two_words[two_words.find(' ')+1:]
    return (second+' '+first)

def gather(L,n):
    result=[]
    i=0
    while i<len(L):
        result.append(L[i])
        i=i+n
    return result

def get_keys(L,d):
    result=[]
    for  k in d:
        if k in L:
            result.append(k)
    return result

def are_lengths(L1,L2):
    result=True
    for i in range(len(L1)):
        if L1[i]!=len(L2[i]):
            result=False
    return result

    return result
