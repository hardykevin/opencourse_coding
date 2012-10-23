# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
import copy
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    result=0
    xlist=[pow(x,n) for n in range(len(poly))]
    for polyitem,xitem in zip(poly,xlist):
        result+=polyitem*xitem
    return result/1.0






# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...
    if len(poly)==1:
        return [0.0]
    else:
        xpow=[n for n in range(len(poly))]
        newpoly=[]
        for p,x in zip(poly,xpow):
            newpoly.append(p*x*1.0)
        return newpoly[1:] 



count=0
# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
    if abs(evaluatePoly(poly,x_0))<epsilon:
        exts=copy.deepcopy(globals()['count'])
        globals()['count']=0
        return [x_0,exts]
    else:
        dpoly=computeDeriv(poly)
        newx=x_0-evaluatePoly(poly,x_0)/evaluatePoly(dpoly,x_0)
        globals()['count']+=1
        print "newx=%s,count=%s,epsilon=%s" % (evaluatePoly(poly,newx),globals()['count'],epsilon)
        return computeRoot(poly,newx,epsilon)

print computeRoot([1, 9, 8], -3, .01)
print computeRoot([1, -1, 1, -1], 2, .001)
