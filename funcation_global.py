x = 50

def func():
    
    global x
    
    print('x is',x)
    x = 2
    print('x changed global is',x)

func()
print('x is',x)