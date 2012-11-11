def mystery(s):
    matches=my0
    for i in range(len(s)//2):
        if s[i]==s[len(s)-1-i]:
            matches=matches+1
    return matches==(len(s)//2)

