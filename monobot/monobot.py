import socket
import time
import random
import urllib

#----------------------------------- Settings --------------------------------------#
network = 'irc.goat.chat'
port = 6667
homechan = 'modernpowers'
logchan = 'botlog'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'PASS pjmtpjmt\r\n')
irc.send ( 'NICK monobot\r\n' )
irc.send ( 'USER monobot monobot monobot :Python IRC\r\n' )

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

def Commands(x):
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
	elif info[0] == 'kiwigen':
		Send('https://kiwiirc.com/client/irc.goat.chat:+6697' + data.split('kiwigen ')[1] + '\r\n')
		Botlog('kiwigen consisted of: ' + data.split('kiwigen ')[1] + '\r\n')
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
		if nick == 'Techius':
			Botlog('Techius is being an asshole')
		else:
			Send('monoxane, Polsaker, E-werd, Ravioli, Failure, ping. This guy needs help')
	elif info[0] == 'spam':
		Send('========= SPAM SPAM SPAMMITTY SPAM =========')
	elif info[0] == 'dev':
		Send('DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS')
	elif info[0] == 'developers':
		Send('DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS DEVELOPERS')
	elif info[0] == 'ping':
		Send('pong')
	elif info[0] == 'hi':
		Send('Hi '+ nick + '!')
	elif info[0] == 'fact':
		fact = random.choice(["Rats cannot throw up.", "Iguanas can stay underwater for twenty-eight point seven minutes.", "The moon orbits the Earth every 27.32 days.", "A gallon of water weighs 8.34 pounds.", "The billionth digit of Pi is 9.", "Humans can survive underwater. But not for very long.", "A nanosecond lasts one billionth of a second.", "Honey does not spoil.", "The atomic weight of Germanium is seven two point six four.", "An ostrich's eye is bigger than its brain.", "According to Norse legend, thunder god Thor's chariot was pulled across the sky by two goats.", "The Schrodinger's cat paradox outlines a situation in which a cat in a box must be considered, for all intents and purposes, simultaneously alive and dead. Schrodinger created this paradox as a justification for killing cats.", "You will be dead soon." "Apples. Oranges. Pears. Plums. Kumquats. Tangerines. Lemons. Limes. Avocado. Tomato. Banana. Papaya. Guava.", "Warning, sphere corruption at twenty-- rats cannot throw up.", "Dreams are the subconscious mind's way of reminding people to go to school naked and have their teeth fall out."])
		Send(fact)
	elif info[0] == 'adventure':
		adventure = random.choice(["QUICK: WHAT'S THE SITUATION? Oh, hey, hi pretty lady. My name's Rick. So, you out having a little adventure?", "What, are you fighting that guy? You got that under control? You know, because, looks like there's a lot of stuff on fire...", "Hey, a countdown clock! Man, that is trouble. Situation's looking pretty ugly. For such a beautiful woman. If you don't mind me saying.", "I don't want to scare you, but, I'm an Adventure Sphere. Designed for danger. So, why don't you go ahead and have yourself a little lady break, and I'll just take it from here.", "Here, stand behind me. Yeah, just like that. Just like you're doing. Things are about to get real messy.", "Going for it yourself, huh? All right, angel. I'll do what I can to cover you.", "Doesn't bother me. I gotta say, the view's mighty nice from right here.", "Man, that clock is moving fast. And you are beautiful. Always time to compliment a pretty lady. All right, back to work. Let's do this.", "Did you hear that? I think something just exploded. Man, we are in a lot of danger. This is like Christmas. No, it's better than Christmas. This should be its own holiday. Explosion Day!", "Happy Explosion Day, gorgeous.", "I'll tell ya, it's times like this I wish I had a waist so I could wear all my black belts. Yeah, I'm a black belt. In pretty much everything. Karate. Larate. Jiu Jitsu. Kick punching. Belt making. Taekwondo... Bedroom.", "I am a coiled spring right now. Tension and power. Just... I'm a muscle. Like a big arm muscle, punching through a brick wall, and it's hitting the wall so hard the arm is catching on fire. Oh yeah.", "I probably wouldn't have let things get this far, but you go ahead and do things your way.", "Tell ya what, why don't you put me down and I'll make a distraction.", "All right. You create a distraction then, and I'll distract him from YOUR distraction.", "All right, your funeral. Your beautiful-lady-corpse open casket funeral.", "Do you have a gun? Because I should really have a gun. What is that thing you're holding?", "How about a knife, then? You keep the gun, I'll use a knife."])
		Send(adventure)
	elif info[0] == 'say':
		Send(data.split('say ')[1] + '\r\n')
	elif info[0] == 'archive':
		archiveURL = data.split('archive ')[1]
		archiveURL = urllib.quote_plus(archiveURL)
		Send('https://archive.is/?run=1&url=' + archiveURL +'\r\n')
	elif info[0] == 'repo':
		Send('https://github.com/monoxane/Goat.Chat-Bots')

	else:
		Send("I'm sorry "+ nick +", I'm afraid I can't do that")
	Botlog("Goatchat: " + nick + ' executed ' + str(info).strip('[').strip("'").strip(']').strip("', '").strip("\r\n'"))

#------------------------------------------------------------------------------#
while True:
    action = 'none'
    data = irc.recv ( 4096 )
    print data

    if data.find ( 'End of message of the day.' ) != -1:
            Join(homechan)
            Join(logchan)
            irc.send('MODE monobot +B \r\n')
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

			if data.find('1984') != -1:
				Send('     WAR IS PEACE     ')
				Send('  FREEDOM IS SLAVERY  ')
				Send('IGNORANCE IS STREANGTH')

			if data.find('monobot, ') != -1:
				x = data.split('#')[1]
				x = x.split('monobot, ')[1]
				Commands(x)
			elif data.find('monobot: ') != -1:
                                x = data.split('#')[1]
                                x = x.split('monobot: ')[1]
				Commands(x)

		if action == 'JOIN':
			open("joinlog.txt", 'a').write("Goatchat: " + data)
			time.sleep(0.5)
			nick = data.split('!')[0]
			nick = nick.replace(':', ' ')
			nick = nick.replace(' ', '')
			nick = nick.strip(' \t\n\r')
			normal = random.choice(["Welcome Back", "Hello", "Welcome"])
			rare = random.choice(["Welcome... to the desert of the real.", "So, wake up," + nick + ". Wake up and... *smell the ashes*...", "Hello, and again, welcome to the Aperture Science Enrichment Center."])
			if nick == 'hydra':
				Send('HAIL HYDRA')
			else:
				for line in file('joinlog.txt'):
					if nick in line:
						Send('Welcome To The Matrix, ' +nick)
						break
					else:
						Send(random.choice([normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, rare]) + ' ' + nick)
					break
