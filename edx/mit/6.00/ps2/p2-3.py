balance =3329 
annualInterestRate = .2
low = balance/12
high = (balance * (1 + annualInterestRate/12)**12)/12
monthlyInterestRate = (1 + (annualInterestRate/12))
newBalance = balance 
while abs(newBalance) >= .01:
    newBalance=balance
    payment =(low + high)/2
    print([low,payment,high].sort())
    for month in range(12):
        newBalance = (newBalance - payment) * (monthlyInterestRate)
    print(newBalance,payment)
    if newBalance > 0.01:
        low = payment
    else:
        high = payment
print('Lowest Payment: ' + str(round(payment,2)))
