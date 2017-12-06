try:
    inp = raw_input("Enter Score: ")
    score = float(inp)
except:
    print "error, please enter a float beteen 0.0 and 1.0."
    quit()
if score >= 0.9:
    print "A"
elif score >= 0.8:
    print "B"
elif score >= 0.7:
    print "C"
elif score >= 0.6:
    print "D"
else:
    print "F"

