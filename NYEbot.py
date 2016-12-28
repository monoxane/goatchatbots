import socket
import time
import random
import datetime
import thread
from multiprocessing import Queue

global timestr
timestr = datetime.datetime.now().strftime("%H:%M:%S")
global snd
snd = ''
global data

def NYEbot():
   network = 'irc.goat.chat'
   port = 6667
   irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
   irc.connect ( ( network, port ) )
   irc.send ( 'NICK NYEbot\r\n' )
   irc.send ( 'USER NYEbot monobot monobot :Python IRC\r\n' )
   irc.send ( 'JOIN #monotest\r\n' )
   time.sleep(10)
   irc.send ( 'PRIVMSG nickserv identify sysadmin\r\n' )
   irc.send ( 'JOIN #monotest\r\n' )
   while True:
      snd =''
      timestr = datetime.datetime.now().strftime("%H:%M:%S:%3")
      irc.send( 'PRIVMSG #monotest :'+timestr+snd+'\r\n' )
      print(timestr)
   while True:
      data = irc.recv ( 4096 )
      print(data)
      if data.find ( 'PING' ) != -1:
         irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
         
      snd =''
      timestr = datetime.datetime.now().strftime("%H:%M:%S")
      irc.send( 'PRIVMSG #monotest :'+timestr+snd+'\r\n' )
      snd =''
      print(timestr)
   print(data)
   
   while True:
      snd =''
      timestr = datetime.datetime.now().strftime("%H:%M:%S")
      irc.send( 'PRIVMSG #monotest :'+timestr+snd+'\r\n' )
      print(timestr)

def Send(msg):
   irc.send('PRIVMSG #monotest :' + msg +  '\r\n')
   
def NYEtime():
   while 1 == 1:
      timestr = datetime.datetime.now().strftime("%H:%M:%S")
      time.sleep(1)
      timestr = ''

def NYEcounts():
   while True:
      timestr = datetime.datetime.now().strftime("%H:%M:%S:%3")
      if timestr == '21:14:00:000':
         global snd
         snd = 'FMTNY2017'
         print('FMTNYD2017\r')
   
timeq = Queue()
sndq = Queue()

thread.start_new_thread(NYEtime, ())
thread.start_new_thread(NYEbot, ())
thread.start_new_thread(NYEcounts, ())
