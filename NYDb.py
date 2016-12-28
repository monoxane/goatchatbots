import socket
import time
import random
import datetime
import thread
from multiprocessing import Queue

#----------------------------------- Settings --------------------------------------#

network = 'irc.goat.chat'
port = 6667
homechan = 'monotest'
logchan = 'monotest'

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

def MainBot():


    while 1 == 1:
        
            action = 'none'

            data = irc.recv ( 4096 )
            print data+'\r'
            
            if data.find ( 'End of message of the day.' ) != -1:
                    Join(homechan)
                    Join(logchan)
                    irc.send('MODE NYDbot +B \r\n')
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
                                if data.find('NYDbot') != -1:
                                        Send('Canberra, Vladivostok, Port Moresby: FIVE MINUTES TO NEW YEARS 2017!')

                        timestr = datetime.datetime.now().strftime("%H:%M:%S:")
                        if timestr == '2:09:00':
                               if snd1 == 0:
                                       timeq.put('FMTNY2017')
                                       print('FMTNYD2017')
                                       snd1 = 1
                               elif snd1 == 1:
                                       print('alreadysnt')

#------------------------------------------------------------------------------#

irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'PASS pjmtpjmt\r\n')
irc.send ( 'NICK NYDbot\r\n' )
irc.send ( 'USER monobot monobot monobot :Python IRC\r\n' )
    
timeq = Queue()
MainBot()
