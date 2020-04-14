#w3b13locker by Samartha
import sys
import config as c
hostsFile=r'hosts.txt'
#hostsFile=c.config()
def searchDomain(dom):
    flag=0
    index=0
    sHosts = open(hostsFile,'r')
    dList=sHosts.read().split('\n')
    for lines in dList:
        if '#' not in lines and lines!='\n' and lines!='':
            xDom=lines.split(' ')
            # print(xDom)
            if dom == xDom[1]:
                flag=1
                break
        index+=1
    sHosts.close()
    if flag==1:
        return index
    else:
        return -1
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
        if searchDomain(domain)>=0:
            print(domain, ' is already blocked')
        else:
            wHost=open(hostsFile,'a')
            wHost.write('\n')
            block='127.0.0.1 ' + domain
            wHost.write(block)
            wHost.close()
    elif option=='-ub' or option=='--unblock' :
        index=searchDomain(domain)
        if index>=0:
            rHost=open(hostsFile,'r')
            dList=rHost.read().split('\n')
            rHost.close()
            wHost=open(hostsFile,'w')
            for dom in dList:
                if '#' in dom :
                    wHost.write(dom+'\n')
                if '#' not in dom and dom!='\n' and dom!='':
                     xDom=dom.split(' ')
                     if domain!=xDom[1]:
                         wHost.write(xDom[0]+' '+xDom[1]+'\n')
            wHost.close()
        else:
            print(domain , ' domain is not in the hosts')
    elif option=='-s' or option=='--search' :
        index=searchDomain(domain)
        if index>=0:
            wHost=open(hostsFile,'r')
            x=wHost.read().split('\n')
            print(domain , 'is present at line ' ,index+1,'\n', x[index])
            wHost.close()
        else:
            print(domain , ' domain is not in the hosts')
    else:
        print('Invalid argument\nUse -h/--help to display valid options')
