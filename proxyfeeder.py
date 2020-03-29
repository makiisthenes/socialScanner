#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import time
import itertools
import threading
import sys

Green = "\033[1;33m"
Blue = "\033[1;34m"
Grey = "\033[1;30m"
Reset = "\033[0m"
Red = "\033[1;31m"
Purple = "\033[0;35m"


print("           "+Green+"   #################################")
print( "           "+Green+"           -PROXY FEEDER ")
print("           "+Green+"     ############################")
print("           "+Green+"       [+]: CODED BY MRANONYMOUSTZ :[+]")
print("           "+Green+"        ########################")
print("")
print("           "+Grey+" █║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║█")
print("    "+Green+" just take a beer i will take care everything for you")
print("           "+Blue+"")

done = False


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rWAIT NICA LEM DO IT QUICKLY ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('')


t = threading.Thread(target=animate)
t.start()
time.sleep(10)
done = True
print(""+Purple+"---> I FOUND THESE.......")
time.sleep(3)
print(""+Blue+"")

proxyDomain = "https://free-proxy-list.net" # KAMA ukichange hii ujue kutafuta table na id ya host unayemtaka

system = requests.get(proxyDomain)

mranonymous_systemSoup = BeautifulSoup(system.content,'html.parser')

sosBlackhats = mranonymous_systemSoup.find('table',{"id" : "proxylisttable"})

for row in sosBlackhats.find_all('tr'):
    columns = row.find_all('td')
    try:
        print(r"%s:%s\t%-20s\t%-10s" % (columns[0].get_text(), columns[1].get_text(), columns[3].get_text(), columns[4].get_text()))
    except Exception as e:
        pass

print(" "+Grey+" JUST RUN ME ANYTIME, I WILL REFRESH PROXY LIST < join US on irc #HackersUnity server= freenode >")

    






 

