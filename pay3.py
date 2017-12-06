def computepay(h,r):
    if (h<=40):
        return h*10.5
    else:
        return (40*10.5+(h-40)*10.5*1.5)

hrs = raw_input("Enter Hours: ")
hrs = float(hrs)
rts = raw_input("Enter Rate: ")
rts = float(rts)
p = computepay(hrs,rts)
print p