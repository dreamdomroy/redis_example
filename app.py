import redis
from rq import Queue
from function.randomTime import randomCountDown
import time

# 建立redis類別的物件con，可以想像成一個專注於排序的伺服器
con = redis.Redis()

# 使用rq模組內的Queue函式來建立佇列物件q。
# 第一個參數是佇列的名字，參數connection則是他要連線的排序伺服器。
q = Queue('default', connection=con)

nameList = ['Austin','Brian','Cherry']
for name in nameList:
    j = q.enqueue(randomCountDown,name)
checkTime = 1
for i in range(15):
    print(checkTime)
    time.sleep(1)
    checkTime += 1