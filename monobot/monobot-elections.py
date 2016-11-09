import socket
import time
import random
import urllib
import json
import requests
from lxml import html

#----------------------------------- Settings --------------------------------------#

network = 'irc.goat.chat'
port = 6667
homechan = 'happening'
logchan = 'botlog'

#---------------------------------- Functions -------------------------------------#

def Send(msg):
	irc.send('PRIVMSG #' + homechan + ' :' + msg +  '\r\n')

def Botlog(logmsg):
	irc.send('PRIVMSG #' + logchan + ' :' + logmsg +  '\r\n')
	open("botlog.txt", 'a').write(logmsg +'\n')


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

irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'PASS pjmtpjmt\r\n')
irc.send ( 'NICK monobot-elections\r\n' )
irc.send ( 'USER monobot-elections monobot monobot :Python IRC\r\n' )

while True:
    action = 'none'
    data = irc.recv ( 4096 )
    print data

    if data.find ( 'End of message of the day.' ) != -1:
            Join(homechan)
            Join(logchan)
            irc.send('MODE monobot-elections +B \r\n')
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

                        if data.find('`results') != -1:
							page = requests.get('https://ig.ft.com/us-elections/results')
							tree = html.fromstring(page.content)
							hillary = tree.xpath("//div[@id='president-datalabel-clinton']")[0].text
							trump = tree.xpath("//div[@id='president-datalabel-trump']")[0].text
							Send('Hillary: ' + str(hillary) + ', Trump: ' + str(trump))
