import sys
import time

f = None
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end='')
        sys.stdout.flush()
        print('Press ctrl+c now')

        # 为了确保程序运行一段时间
        time.sleep(2)
except IOError :
    print('Could not find file poem.txt')
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if  f:
        f.close()
    print('Cleanning up: Closed the file')





    # Navicat premuim
    # axure
    # StarUML
    # Intellij