def laceStrings(s1,s2):
    strdic={len(s1):s1,len(s2):s2}
    newstr=''
    maxlen=max(len(s1),len(s2))
    minlen=min(len(s1),len(s2))
    for index in range(minlen):
        newstr+=s1[index]+s2[index]
    newstr+=strdic[maxlen][minlen:]
    return newstr
