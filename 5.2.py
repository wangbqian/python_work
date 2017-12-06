largest = None
smallest = 10000
while True:
    num = raw_input("Enter a integer number: ")
    if num == "done" : 
        break
    else:
        try:
            num = int(num)
        except:
            print "Invalid input"
            continue
        smallest = min(num,smallest)
        largest = max(num,largest)

print "Maximum is ", largest
print "Minimum is ", smallest