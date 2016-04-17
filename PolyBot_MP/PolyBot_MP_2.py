import socket
import sys
from random import randint
import re
import time
import random

#----------------------------------- Settings --------------------------------------#
network = 'irc.goat.chat'
port = 6667
homechan = 'modernpowers'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'PASS pjmtpjmt\r\n')
irc.send ( 'NICK PolyBot\r\n' )
irc.send ( 'USER PolyBot PolyBot PolyBot :Python IRC\r\n' )
#----------------------------------------------------------------------------------#

#---------------------------------- Functions -------------------------------------#

def Send(msg):
	irc.send('PRIVMSG #' + homechan + ' :' + msg +  '\r\n')
	
def Botlog(logmsg):
	irc.send('PRIVMSG #PolyBotLogging :' + logmsg + '\r\n')
	open("botlog.txt", 'a').write(logmsg)
	

def Join(chan):
	irc.send ( 'JOIN #' + chan + '\r\n' )

def Part(chan):
	irc.send ( 'PART #' + chan + '\r\n' )

def NewNick():
	datafile = file('joinlog.txt')
	for line in datafile:
		if nick in line:
			found = True
			break
	return found



#------------------------------------------------------------------------------#
while True:
    action = 'none'
    data = irc.recv ( 4096 )
    print data

    if data.find ( 'End of message of the day.' ) != -1:
            Join(homechan)
            Join('PolyBotLogging')
            irc.send('MODE PolyBot +B')
            time.sleep(2)
            data = ''

    if data.find ( 'PING' ) != -1:
            irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )


    #--------------------------- Action check --------------------------------#
    if data.find('#') != -1:
        action = data.split('#')[0]
        action = action.split(' ')[1]

    if data.find('NICK') != -1:
        if data.find('#') == -1:
            action = 'NICK'

    #----------------------------- Actions -----------------------------------#
    if action != 'none':

		if action == 'PRIVMSG':

			if data.find('PolyBot, ') != -1:
				x = data.split('#')[1]
				x = x.split('PolyBot, ')[1]
				info = x.split(' ')
				info[0] = info[0].strip(' \t\n\r')

				nick = data.split('!')[0]
				nick = nick.replace(':', ' ')
				nick = nick.replace(' ', '')
				nick = nick.strip(' \t\n\r')

				if info[0] == 'info':
					Send('This is the IRC channel for Modern Powers,' )
					Send('We are a country roleplaying game' )
					Send('We are based at v/modernpowers' )
					Send('For more info go to:\00310 https://voat.co/v/modernpowers\003' )
					Send('For the rules go to:\00310 http://goo.gl/54sgp3\003' )
				elif info[0] == 'poem':
					Send('Do not go gentle into that good night,')
					Send('Old age should burn and rave at close of day;')
					Send('Rage, rage against the dying of the light.')
					Send(' ')
					Send('Though wise men at their end know dark is right,')
					Send('Because their words had forked no lightning they')
					Send('Do not go gentle into that good night.')
				elif info[0] == 'claim':
					Send('Claims Info,')
					Send('Current Claimed and Unclaimed Countries:\00310 https://goo.gl/1TClzP \003 ')
					Send(' ')
					Send('Claims Form:\00310 https://goo.gl/LWhZii\003')
				elif info[0] == 'irchelp':
					if nick == 'Techius' or 'techius':
						print('techius')
					else:
						Send('monoxane, Polsaker, E-werd, Ravioli, Failure, ping. This guy needs help')
				elif info[0] == 'ping':
					Send('pong')
				elif info[0] == 'hi':
					Send('Hi '+ nick + '!')
				else:
					Send("I'm sorry "+ nick +", I'm afraid I can't do that")
					
				SendBotlog(nick + ' executed ' +info)
				
		if action == 'JOIN':
			open("joinlog.txt", 'a').write(data)
			time.sleep(0.5)
			wb = random.choice(["Welcome Back", "Hello", "Welcome"])
			nick = data.split('!')[0]
			nick = nick.replace(':', ' ')
			nick = nick.replace(' ', '')
			nick = nick.strip(' \t\n\r')
			datafile = file('joinlog.txt')
			for line in datafile:
				if nick in line:
					Send('Welcome To The Matrix, ' +nick)
					break
				else:
					Send(wb + ' ' + nick)
					break
