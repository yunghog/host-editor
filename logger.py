#write log.ini
#author : Samartha
import datetime as dt
def log(logDetails):
    logFile=open(r'data/log.ini','a+')
    now = dt.datetime.now()
    now = now.strftime("%Y-%m-%d_%H:%M:%S")
    logFile.write(now+'_'+logDetails+'\n')
    logFile.close()
