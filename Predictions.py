# -*- coding=UTF-8 -*-
# essai de programme commencé le 02/10/2012 et terminé le 03/10/2012

import time
"""La fonction 'time.sleep' permet de marquer un arrêt dans le script"""

name = raw_input("What is your name? \n \t> ")
print "Hello %r" % name
time.sleep(2)
print "Wellcome!"
time.sleep(2)
print "I will predict your future."
time.sleep(2)
print "Answer the following questions carefully."
time.sleep(2)
print "What is your favorite color?"
color = raw_input("Type '1' for red, '2' for blue \n \t> ")
time.sleep(2)
print "What is your childhood dream?"
dream = raw_input("Type '1' for going to the moon, '2' for swimming with dolphins \n \t> ")
time.sleep(2)
print "Are you ready to hear this revelation?"
time.sleep(2)
ready = raw_input("If you feel ready type 'Yes', otherwise type 'No' \n \t> ")
time.sleep(2)
if ready == "No":
	print "Too bad for you!"
if ready == "Yes":
	print "Very good! Here is my prediction :"
	time.sleep(2)
	if color == "1" and dream == "1":
		print " * You are destined for Exploring the world * "
	elif color == "1" and dream == "2":
		print " * You are destined for Protecting others * "
	elif color == "2" and dream == "1":
		print " * You are destined for Creating a better world * "
	elif color == "2" and dream == "2":
		print " * You are destined for Inspiring people * "
	else:
		print "It seems you did not answer correctly"
time.sleep(2)
print "Good Bye! =)"
