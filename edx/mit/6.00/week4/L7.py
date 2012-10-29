def rem(x,a):
    print x
    if x==a:
        print "excute if"
        return 0
    elif x<a:
        print "excute elif"
        return x
    else:
        print "excute else"
        rem(x-a,x)

rem(7,5)
