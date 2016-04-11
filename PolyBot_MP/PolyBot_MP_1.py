import socket
import time
import random

network = 'irc.goat.chat'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
irc.send ( 'NICK PolyBot\r\n' )
irc.send ( 'USER PolyBot PolyBot PolyBot :Python IRC\r\n' )
irc.send ( 'JOIN #modernpowers\r\n' )
time.sleep(10)
irc.send ( 'PRIVMSG nickserv identify <pass>\r\n' )

while True:
   data = irc.recv ( 4096 )
   print(data)
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( 'KICK' ) != -1:#kick+rejoin
      irc.send ( 'JOIN #modernpowers\r\n' )
   if data.find ( 'PolyBot, claims' ) != -1:
      irc.send ( 'PRIVMSG #modernpowers :Claims Info,\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Current Claimed and Unclaimed Countries:\r\n' )
      irc.send ( 'PRIVMSG #modernpowers : \00310    https://goo.gl/1TClzP\003 \r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Claims Form:\r\n' )
      irc.send ( 'PRIVMSG #modernpowers : \00310    https://goo.gl/LWhZii\003 \r\n' )
   if data.find ( 'PolyBot, info' ) != -1:
      irc.send ( 'PRIVMSG #modernpowers :This is the IRC channel for Modern Powers,\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :We are a country roleplaying game\r\n' )
      irc.send ( 'PRIVMSG #modernpowers : \r\n' )
      irc.send ( 'PRIVMSG #modernpowers :We are based at v/modernpowers\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :For more info go to:\00310 https://voat.co/v/modernpowers\003 \r\n' )
      irc.send ( 'PRIVMSG #modernpowers :For the rules go to:\00310 http://goo.gl/54sgp3\003\r\n' )
   if data.find ( 'PolyBot, poem' ) != -1:#hi
      irc.send ( 'PRIVMSG #modernpowers :Do not go gentle into that good night,\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Old age should burn and rave at close of day;\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Rage, rage against the dying of the light.\r\n' )
      irc.send ( 'PRIVMSG #modernpowers : \r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Though wise men at their end know dark is right,\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Because their words had forked no lightning they\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Do not go gentle into that good night.\r\n' )
   if data.find ( 'PolyBot, spam' ) != -1:#spam
      irc.send ( 'PRIVMSG #modernpowers : ==== SPAM, SPAM, SPAM, SPAMMITY SPAM! ==== \r\n' )
   if data.find ( 'JOIN :#modernpowers' ) != -1:#joins
      time.sleep(2)
      wb = random.choice(["Welcome Back!", "Hello!", "Welcome!"])
      irc.send ( 'PRIVMSG #modernpowers :' + wb + '\r\n' )
      open("joinlog.txt", 'a').write(data)
   if data.find ( 'PolyBot, test' ) != -1: #test
      irc.send ( 'PRIVMSG #modernpowers :Pong, Working now?\r\n' )
print(data)
