
import datetime
from mongoengine.connection import connect

if __name__ == "__main__":
    print "nihao";
    #计算今天的时间
    today = datetime.date.today()
    print today
    #计算昨天的时间 
#     yesterday = today - datetime.timedelta(days = 1)
#     print yesterday