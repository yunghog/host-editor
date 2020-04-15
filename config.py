#cofigure the w3b13locker
#author : Samartha
import platform
import os
def config() :
    myos=platform.system()
    if myos=='Windows':
        windir=os.environ['windir']
        hostPath=windir+r'\system32\drivers\etc\hosts'
    if myos=='Linux':
        hostPath=r'/etc/hosts'
    pathFile=open(r'data/path.txt','w')
    pathFile.write('operatingSystem|'+myos+'\n'+'hosts|'+hostPath+'\n')
    return hostPath
