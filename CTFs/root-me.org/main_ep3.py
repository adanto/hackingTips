#!/usr/bin/env python

import socket, string, time, thread, random
import codecs
from math import sqrt
SERVER = 'irc.root-me.org'
PORT = 6667
NICKNAME = "".join( [random.choice(string.letters[:26]) for i in xrange(15)] )
CHANNEL = '#root-me_challenge'

def main():
	global IRC
	IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	IRC.connect((SERVER, PORT))
	Listener()

def Listener():

	b = IRC.recv(2048)
	print b
	raw_input("Press intro to send username...")

	IRC.send("NICK " + NICKNAME + "\r\n")
	raw_input("Press intro to send user,,")
	IRC.send("USER keypatcher irc.root-me.org root-me :keypatcher\r\n")
	
	b = IRC.recv(1024)
	print b
	
	raw_input("Press intro to join...")
	IRC.send("JOIN  " + CHANNEL + "\r\n")
		
	b = IRC.recv(4098)
	print b
	
	raw_input("Press intro to send priv msg")
	

	IRC.send("PRIVMSG Candy :!ep3 \r\n")
	time.sleep(1)
	
	b = IRC.recv(2048)
	
	print "->", b, "<-"

	b = b.split(':')[-1]

	print b
	
	a1 = b.split()[0]

	print "PRIVMSG Candy :!ep3 -rep %s" % codecs.encode(a1,'rot_13')

	IRC.send("PRIVMSG Candy :!ep3 -rep %s\r\n" % codecs.encode(a1,'rot_13'))

	print "SENT"
	time.sleep(2)
	print "What is this saying.."

	b = IRC.recv(1024)
	print b

if __name__ == '__main__':
	main()





#:Candy!Candy@root-me.org PRIVMSG keypatcher :83 / 6705