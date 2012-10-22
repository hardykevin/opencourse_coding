balance = 320000 
annualInterestRate = 0.2 
steps=1
payment=10
while True:
    remain=balance
    for m in range(12):
        remain=round((remain-payment)*(1+annualInterestRate/12),2)
        steps+=1
        print('There are '+ str(steps)+' steps.')
    if remain<=0:
        break
    else:
        payment+=10

print("Lowest Payment: "+str(payment))
