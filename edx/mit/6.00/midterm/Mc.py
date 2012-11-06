def McNuggets(n):
    times=0
    def rec(n):
        locals()['times']+=1
        print times
        if n%6==0 or n%9==0 or n%20==0:
            return True
        elif times==3:
            return False
        elif n%6!=0:
            return rec(n%6)
        elif n%9!=0:
            return rec(n%9)
        elif n%20!=0:
            return rec(n%20)
    return rec(n)
        
