import socket
import time
import random

network = 'irc.goat.chat'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
irc.send ( 'NICK NCP\r\n' )
irc.send ( 'USER PolyBot PolyBot PolyBot :Python IRC\r\n' )
irc.send ( 'JOIN #newcountryproject\r\n' )
time.sleep(10)
irc.send ( 'PRIVMSG nickserv identify pjmtpjmt\r\n' )

def Send(msg):
  irc.send('PRIVMSG #newcountryproject:' + msg + ' \r\n')
  
while True:
    data = irc.recv ( 4096 )
    print(data)
    if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
    if data.find ( 'NCP, info' ) != -1: #leave
      Send('This is the irc channel for v/newcountryproject')
    if data.find('JOINS'):
        time.sleep(0.5)
        wb = random.choice(["Welcome Back", "Hello", "Welcome"])
        nick = data.split('!')[0]
        nick = nick.replace(':', ' ')
        nick = nick.replace(' ', '')
        nick = nick.strip(' \t\n\r')
        Send(wb + ' ' + nick)
print(data)
