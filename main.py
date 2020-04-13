#w3b13locker by Samartha
import sys
hostsFile=r'hosts.txt'
# rHost=open(r'hosts.txt','r')
argc = len(sys.argv)
if argc>1 and argc<=4 :
    option = sys.argv[1]
    if argc==4 :
        option2 = sys.argv[2]
        dList = sys.argv[3]
    elif argc==3 :
        domain = sys.argv[2]
else:
    print('Invalid set of arguments\nUse -h/--help to display valid options')
if argc==2 :
    if option=='-l' or option=='--list' :
        rHost=open(hostsFile,'r')
        for line in rHost :
            if line[0] != '#' :
                print(line, end='')
        rHost.close();
    elif option=='-h' or option=='--help' :
        print('all the possible option combinations !!')
    else:
        print('Invalid argument\nUse -h/--help to display valid options')
if argc==3 :
    if option=='-b' or option=='--block' :
        wHost=open(hostsFile,'a')
        wHost.write('\n')
        block='127.0.0.1\t' + domain
        wHost.write(block)
        wHost.close()
    else:
        print('Invalid argument\nUse -h/--help to display valid options')
