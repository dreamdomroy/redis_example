import time
import random
def randomCountDown(name):
    rt = 10
    print('程序{}，執行{}秒'.format(name,rt))
    for i in range(1,rt+1):
        time.sleep(1)
        print(i)
    print('程序{}結束'.format(name))