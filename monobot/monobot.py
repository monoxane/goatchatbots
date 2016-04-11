import socket
import sys
from random import randint
import re
import time
import random

joinlog_file = file('joinlog.txt')
wb = random.choice(["Welcome Back", "Hello", "Welcome"])

#----------------------------------- Settings --------------------------------------#
network = 'irc.goat.chat'
port = 6667
homechan = '#voat'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'PASS pjmtpjmt\r\n')
irc.send ( 'NICK monobot\r\n' )
irc.send ( 'USER monobot monobot monobot :monobot\r\n' )
#----------------------------------------------------------------------------------#

#---------------------------------- Functions -------------------------------------#

def Send(chan, msg):
	irc.send('PRIVMSG ' + chan + ' :' + msg +  '\r\n')

def Join(chan):
	irc.send ( 'JOIN ' + chan + '\r\n' )

def Part(chan):
	irc.send ( 'PART ' + chan + '\r\n' )

def new_user():
	datafile = file('joinlog.txt')
	for line in datafile:
		if nick in line:
			return True
			break
	return False

def get_nick():
	nick = data.split('!')[0]
	nick = nick.replace(':', ' ')
	nick = nick.replace(' ', '')
	nick = nick.strip(' \t\n\r')

def get_chan():
	msg_chan = data.split('PRIVMSG ')[1]
	msg_chan = msg_chan.split(' :')[0]

	#:monoxane!monoxane@goat-helper/monoxane PRIVMSG #modernpowers :gotta do some research

	#------------------------------------------------------------------------------#
while True:
	action = 'none'
	data = irc.recv ( 4096 )
	print data

        if data.find ( 'Welcome to...' ) != -1:
            Join(homechan)
            irc.send('MODE monobot +B')
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

		if data.find('monobot, ') != -1:
                        x = data.split('#')[1]
                        x = x.split('monobot, ')[1]
                        info = x.split(' ')
                        info = str(info[0].strip(' \t\n\r'))
                        get_chan()

		if info == 'info':
			if msg_chan == '#modernpowers':
                            Send('#modernpowers', 'We are a country roleplaying game' )
                            Send('#modernpowers', 'We are based at v/modernpowers' )
                            Send('#modernpowers', 'For more info go to:\00310 voat.co/v/modernpowers\003' )
                            Send('#modernpowers', 'For a starters guide go to:\00310 http://goo.gl/1xsyR3\003' )
                            Send('#modernpowers', 'For the rules go to:\00310 http://goo.gl/eiXwlL\003' )
                            Send('#modernpowers', 'And for a timeline of events go to:\00310 http://goo.gl/alZZvM \003' )
		elif msg_chan == '#!':
			Send('#!', 'This is a channel to chat and shit, Orange and green are us, Polsaker runs this thing and blue are bots')

		elif info == 'poem':
			Send(msg_chan, 'Do not go gentle into that good night,')
			Send(msg_chan, 'Old age should burn and rave at close of day;')
			Send(msg_chan, 'Rage, rage against the dying of the light.')
			Send(msg_chan, ' ')
			Send(msg_chan, 'Though wise men at their end know dark is right,')
			Send(msg_chan, 'Because their words had forked no lightning they')
			Send(msg_chan, 'Do not go gentle into that good night.')

		elif info == 'claim':
			if msg_chan == '#modernpowers':
                            Send('#modernpowers', 'Claims Info,')
                            Send('#modernpowers', 'Current Claimed and Unclaimed Countries:\00310 https://goo.gl/v5X7i7 \003 ')
                            Send('#modernpowers', ' ')
                            Send('#modernpowers', 'Claims Form:\00310 https://goo.gl/awtdj6\003')
		elif info == 'ping':
			Send(msg_chan, 'pong')

		else:
					nick = data.split('!')[0]
					nick = nick.replace(':', ' ')
					nick = nick.replace(' ', '')
					nick = nick.strip(' \t\n\r')
					Send(msg_chan, "I'm sorry "+ nick +", I'm afraid I can't do that")

	if action == 'JOIN':
		get_chan()
		open(joinlog_file, 'a').write(data)
		time.sleep(0.5)
		get_nick()
		if new_user() == True:
					Send(msg_chan,'Welcome To The Matrix, ' +nick)
					break
		else:
					Send(msg_chan, wb + ' ' + nick)
					break
