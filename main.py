#w3b13locker by Samartha
import sys
import os
import config as c
import logger as l
banner="""
    ██╗    ██╗███████╗██████╗       ██████╗ ██╗      ██████╗  ██████╗██╗  ██╗███████╗██████╗
    ██║    ██║██╔════╝██╔══██╗      ██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ██║ █╗ ██║█████╗  ██████╔╝█████╗██████╔╝██║     ██║   ██║██║     █████╔╝ █████╗  ██████╔╝
    ██║███╗██║██╔══╝  ██╔══██╗╚════╝██╔══██╗██║     ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ╚███╔███╔╝███████╗██████╔╝      ██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
    ╚══╝╚══╝ ╚══════╝╚═════╝       ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                ---by Samartha---
"""
hostsFile=r'hosts.txt'
# hostsFile=c.config()
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
        os.system('cls')
        print('------------hosts-------------')
        rHost=open(hostsFile,'r')
        for line in rHost :
            if line[0] != '#' :
                print(line, end='')
        rHost.close();
    elif option=='-h' or option=='--help' :
        os.system('cls')
        help='''Usage: python main.py [option] [arguments]
        python main.py [-b/-ub/-s/-h/l/--block/--unblock/--search/--list/--help] *[-f/--file] *[domain/domain list]\n
+----------------+-----------------------------------------------+
| option         | description                                   |
+----------------+-----------------------------------------------+
| -b/--block     | blocks the domain. takes domain as argument   |
| -ub/--unblock  | unblocks the domain. takes doamin as argument |
| -s/--search    | search for a domain. takes domain as argument |
| -l/--list      | list blocked domain                           |
| -f/--file      | used along with -b/--block or -ub/--unblock.  |
|                | takes domain list                             |
+----------------+-----------------------------------------------+
                 ----------w3b13locker----------
                    ---stable build v1.1---
                        --by Samartha--
'''
        print(banner)
        print(help)
    else:
        print('Invalid argument\nUse -h/--help to display valid options')
if argc==3 :
    if option=='-b' or option=='--block' :
        if searchDomain(domain)>=0:
            print(domain, ' is already blocked')
        else:
            try:
                wHost=open(hostsFile,'a')
                wHost.write('\n')
                block='127.0.0.1 ' + domain
                wHost.write(block)
                wHost.close()
                l.log('blocked_'+domain)
            except PermissionError :
                l.log('failed_to_block_'+domain+'_Error:Access denied')
                print('Failed! Access denied! Open console with admin rights')
    elif option=='-ub' or option=='--unblock' :
        index=searchDomain(domain)
        if index>=0:
            try:
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
                l.log('unblocked_'+domain)
            except PermissionError :
                l.log('failed_to_unblock_'+domain+'_Error:Access denied')
                print('Failed! Access denied! Open console with admin rights')
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
if argc==4:
    if option=='-b' or option=='--block' and option2=='-f' or option2=='--file' :
        try:
            wHosts=open(hostsFile,'a')
            domainFile=open(dList,'r')
            domains=domainFile.read().split('\n')
            for i in domains:
                if i!='':
                    wHosts.write('\n')
                    block='127.0.0.1 ' + i
                    wHosts.write(block)
                    l.log('blocked_'+i+'_by_file_'+dList)
            wHosts.close()
            domainFile.close()
        except Exception as e:
            print(e)
            print('File Error while reading')
    else:
        print("Invalid argument\nUse -h/--help to display valid options")
