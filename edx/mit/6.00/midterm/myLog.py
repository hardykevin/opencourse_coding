import math
def myLog(x,b):
    guess=0
    while True:
        if b**(guess+1)>x:
            return guess
        else:
            guess+=1
   
def test_myLog(x,b):
    if myLog(x,b)==math.floor(math.log(x,b)):
        print "correct"
    else:
        print "Wrong! For log_%s(%s),it is should be %s" % (b,x,math.floor(math.log(x,b)))
     
