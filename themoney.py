def interest(cMoney,data):
    return cMoney*0.0125/30*data

def defaulItnterest(cMoney,data):
    return cMoney*0.0005*data

Money = 2000
loan_data = 31 
overdue_data = 53

print(interest(Money,loan_data))

print(defaulItnterest(Money,overdue_data))

