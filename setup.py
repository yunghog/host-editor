#setup hosts file and the w3b13locker
#author : Samartha
import time as ti
import tqdm as t
import sys
import os
import config as c
os.system('cls')
print('\n\n')
print('\t██╗    ██╗███████╗██████╗     ██████╗ ██╗      ██████╗  ██████╗██╗  ██╗███████╗██████╗ ')
ti.sleep(.5)
print('\t██║    ██║██╔════╝██╔══██╗    ██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗')
ti.sleep(.5)
print('\t██║ █╗ ██║█████╗  ██████╔╝    ██████╔╝██║     ██║   ██║██║     █████╔╝ █████╗  ██████╔╝')
ti.sleep(.5)
print('\t██║███╗██║██╔══╝  ██╔══██╗    ██╔══██╗██║     ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗')
ti.sleep(.5)
print('\t╚███╔███╔╝███████╗██████╔╝    ██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║')
ti.sleep(.5)
print('\t╚══╝╚══╝ ╚══════╝╚═════╝     ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝')
print('\t\t\t\t\t\t\t\t\t\t\tv0.2\n\t\t\t\t\t\t\t\t\t\t\tby yungh')
print('--------------Setting up hosts--------------')
hosts=c.config()
path=open('data/path.txt','r')
pathInfo=path.read().split('\n')
for line in pathInfo:
    print(line)
path.close()
hostsFile=open(hosts,'r')
hostsBackup=open(r'data/hostsOrginal.txt','w')
hostsData=hostsFile.read().split('\n')
for line in hostsData:
    hostsBackup.write(line+'\n')
hostsBackup.close()
hostsFile.close()
print('--Backup created successfully--')
hostsFile=open(hosts,'w')
for line in hostsData:
    if '#' in line:
        hostsFile.write(line+'\n')
    elif '\t' in line:
        #print(line)
        line=line.split('\t')
        #print(line[0]+' '+line[-1])
        hostsFile.write(line[0]+' '+line[-1]+'\n')
    else:
        hostsFile.write(line+'\n')
hostsFile.close()
print('--Hosts has been modified--')
print('Now you can run main.py')
