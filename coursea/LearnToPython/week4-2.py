def my(s):
    i=0
    result=''
    while not s[i].isdigit():
        result=result+s[i]
        i=i+1
        print(i)

    return result

