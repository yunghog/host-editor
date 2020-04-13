#cofigure the w3b13locker
#author : Samartha
import platform
import os
def config() :
    myos=platform.system()
    if myos=='Windows':
        windir=os.environ['windir']
        hostPath=windir+r'\system32\drivers\etc\hosts'
    return hostPath
