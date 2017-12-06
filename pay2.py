hrs = raw_input("Enter Hours: ")
h = float(hrs)
rts = raw_input("Enter Rate: ")
r = float(rts)
if h > 40:
    salary = 40*r+(h-40)*r*1.5
else:
    salary = 40*r
print salary