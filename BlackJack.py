"""___Blackjack Text-game___
This is a simple BlackJack text-game. The idea is to apply the logic of the game in
a functional programming style.
"""
import random
import sys
import os
import time 

count = 0
dealer_count = 0

def count_cards(cards,count,dealer,dealer_count):
	count = 0
	dealer_count = 0
	values = {("Ac","Ah","As","Ad"):11,("Kc","Kh","Ks","Kd","Qc","Qh","Qs","Qd","Jc","Jh","Js","Jd","10c","10h","10s","10d"):10,
	("9c","9h","9s","9d"):9,("8c","8h","8s","8d"):8,("7c","7h","7s","7d"):7,("6c","6h","6s","6d"):6,("5c","5h","5s","5d"):5,
	("4c","4h","4s","4d"):4,("3c","3h","3s","3d"):3,("2c","2h","2s","2d"):2}
	count_cards.values = values
	#print(card)
	for keys in values.keys():
		for key in keys:
			if key in cards:
				count += values.get(keys)
			if key in dealer:
				dealer_count += values.get(keys)
	#print(count)
	return count,dealer_count
	
def dealer_visible_count(dealer,dealer_count):
	dealer_viscount = 0
	if len(dealer) == 2:
		x = count_cards.values
		for keys in x.keys():
			for key in keys:
				if key == dealer[0]:
					dealer_viscount += x.get(keys)
	else:
		dealer_viscount = dealer_count
	return dealer_viscount
def deck():
	deck = ["Ac","Ah","As","Ad","Kc","Kh","Ks","Kd","Qc","Qh","Qs","Qd","Jc","Jh","Js","Jd","10c","10h","10s","10d",
	"9c","9h","9s","9d","8c","8h","8s","8d","7c","7h","7s","7d","6c","6h","6s","6d","5c","5h","5s","5d","4c","4h","4s","4d",
	"3c","3h","3s","3d","2c","2h","2s","2d"]
	number_of_decks = 1
	deck = deck*number_of_decks
	return deck

def set_name():
	name = input("What is your name? ")
	return name

def set_players():
	players = input("How many players would you like to play with? ")
	return players

def shuffle():
	d = deck()
	random.shuffle(d)
	return d

def draw_game(cards,dealer):
	deck = shuffle()
	#print(deck)
	deck = deal(cards,dealer,deck)
	cards = deck[0]
	dealer = deck[1]
	count = deck[3]
	dealer_count = deck[4]
	deck = deck[2]
	return cards, dealer, deck, count, dealer_count
	
def deal(cards,dealer,deck):
	cards.append(deck[0])
	deck.pop(0)
	dealer.append(deck[0])
	deck.pop(0)
	cards.append(deck[0])
	deck.pop(0)
	dealer.append(deck[0])
	deck.pop(0)
	count1 = count_cards(cards,count,dealer,dealer_count)
	#print(count1)
	count2 = count1[0]
	count3 = count1[1]
	return cards,dealer,deck,count2,count3

def hit(cards,dealer,deck,count,dealer_count):
	cards.append(deck[0])
	deck.pop(0)
	counts = count_cards(cards,count,dealer,dealer_count)
	count = counts[0]
	return cards, dealer, deck, count, dealer_count
	
# def bust(count):
	# if count > 21:
		# print("")
		# print("count: " + str(count))
		# print("")
		# print("BUST")
		# print("BUST")
		# print("BUST")
		# print("BUST")
		# print("")
		# play_again()
		
def ace(cards, dealer, count, dealer_count):
	aces = ["Ac","Ah","As","Ad"]
	for a in aces:
		if a in cards and count > 21:
			count -= 10
		if a in dealer and dealer_count > 21:
			dealer_count -= 10
	return count, dealer_count	

def dealer_turn(count, dealer_count, dealer, deck, cards):
	game = []
	if dealer_count < count:
		game = dealer_hit(dealer,dealer_count, deck, count, cards)
	else:
		print()
		print("Dealer has {0}. You have {1}. You Lose!!".format(dealer_count,count))
		play_again()
	return game
	
def dealer_hit(dealer, dealer_count, deck, count, cards):	
	dealer.append(deck[0])
	deck.pop(0)
	counts = count_cards(cards,count,dealer,dealer_count)
	count = counts[0]
	dealer_count = counts[1]
	return cards, dealer, deck, count, dealer_count
	
def play_again():
	selection = False
	while not selection:
		print()
		answer = input("Would you like to play again (y/n)? ")
		if answer.lower() == 'y':
			blackjack(name)
		elif answer.lower() == 'n':
			quit()
		else:
			print("Invalid Selection. Try Again.")

def intro():
	os.system('cls')
	screen_text = "WELCOME TO MY BLACKJACK GAME!"
	print("")
	print (screen_text)
	print("")
	name = set_name()
	return name
	#players = set_players()

def menu(name,game):
	os.system('cls')
	cards = game[0]
	count = game[3]
	deck = game[2]
	dealer_count = game[4]
	dealer = game[1]
	aceScore = ace(cards,dealer,count,dealer_count)
	count = aceScore[0]
	dealer_count = aceScore[1]
	#print(game)
	dealer_viscount = dealer_visible_count(dealer,dealer_count)
	print("")
	print("Hello " + name + "!")
	print("")
	print("")
	if len(cards) == 2:
		print("Your cards are: " + str(cards[0]) + ", " + str(cards[1]))
	elif len(cards) == 3:
		print("Your cards are: " + str(cards[0]) + ", " + str(cards[1]) + ", " + str(cards[2]))
	elif len(cards)	== 4:
		print("Your cards are: " + str(cards[0]) + ", " + str(cards[1]) + ", " + str(cards[2]) + ", " + str(cards[3]))	
	elif len(cards)	== 5:
		print("Your cards are: " + str(cards[0]) + ", " + str(cards[1]) + ", " + str(cards[2]) + ", " + str(cards[3]) + ", " + str(cards[4]))
	print("")
	print("Count: " + str(count))
	print("")
	if count > 21:
		print("BUST!")
		print("BUST!")
		print("BUST!")
		play_again()
	print("---------------------------------")
	print("")
	if len(dealer) == 2:
		print("Dealer has: " + str(dealer[0]))
	else:
		dealCards = ""
		for i in dealer:
			dealCards += (i + ', ') 
		print("Dealer has: {}".format(dealCards)) 
	print("")
	print("Dealer Count: " + str(dealer_viscount))
	print("")
	print("---------------------------------")
	print("")
	print("")
	if len(dealer) != 2: 
		if dealer_count < 21:
			game = dealer_turn(count, dealer_count, dealer, deck, cards)
			menu(name,game)
		elif dealer_count == 21:
			print()
			print("Dealer has 21. You Lose!")
		else:
			print()
			print("Dealer BUSTED!!!")
			print("YOU WIN!!!!!")
	if len(dealer) == 2:		
		choice = input("Would you like to: \n 1.Hit \n 2.Stay \n\n: ")
		if choice == "1":
			game = hit(game[0],game[1],game[2],game[3],game[4])
			menu(name,game)
		elif choice == "2":
			game = dealer_turn(count, dealer_count, dealer, deck, cards)
			menu(name, game)
	
def blackjack(name):
	cards = []
	dealer = []
	game = draw_game(cards,dealer)
	menu(name,game)
	
name = intro()
blackjack(name)
#Make tie situation event
#Possibly add betting
#Add split/double down etc
