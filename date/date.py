
import datetime
from mongoengine.connection import connect

if __name__ == "__main__":
    print "nihao";
    #��������ʱ��
    today = datetime.date.today()
    print today
    #���������ʱ�� 
#     yesterday = today - datetime.timedelta(days = 1)
#     print yesterday