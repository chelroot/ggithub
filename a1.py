#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
#import time


a = datetime.now() #Проверка
print (a)

b = datetime.strptime( "2009", "%Y" ) # Проверка 2
print (b)

c = datetime.strptime( "2009-11-12 23:18:53", "%Y-%m-%d %H:%M:%S" )
print (c)

g = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
print (g)

gg = datetime.strftime(datetime.now(), "%d.%m")
print (gg)

ggg = datetime.strftime(datetime.now(), "%H")
print (ggg)

dmh = datetime.strftime(datetime.now() + timedelta(hours=-1), "%d.%m")
print (dmh)
print('aaa')

#gggg = datetime.strftime(datetime.now(), "%H").
#ggggg = gggg + timedelta(hours=-1)
#print (ggggg)


t = datetime.now() + timedelta(days=5, hours=-5)
print (t)

tt = datetime.now() + timedelta(hours=-1)
print (tt)

ttt = datetime.strftime(datetime.now() + timedelta(hours=-1), "%H")
print (ttt)

dm7d = datetime.strftime(datetime.now() + timedelta(days=-7), "%d.%m")
print (dm7d)

#http://80.255.89.230/vid74/
#

#e = timedelta(hours=2)
#ee = ggg+e
