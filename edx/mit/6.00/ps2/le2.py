varA=8
varB=-8
if type(varA)=='int' and type(varB)=='int':
    print('two int')
    if varA>varB:
        print('bigger')
    elif varA==varB:
        print('equal')
    else:
        print('smaller')
else:
    print('string involved')
