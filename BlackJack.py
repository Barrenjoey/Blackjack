"""___Blackjack Text-game___
This is a simple BlackJack text-game. The idea is to apply the logic of the game in
a functional programming style.
"""
import random
import sys
import os
import time 

count = 0

def count_cards(card,count):
	count = 0
	values = {("Ac","Ah","As","Ad"):11,("Kc","Kh","Ks","Kd","Qc","Qh","Qs","Qd","Jc","Jh","Js","Jd","10c","10h","10s","10d"):10,
	("9c","9h","9s","9d"):9,("8c","8h","8s","8d"):8,("7c","7h","7s","7d"):7,("6c","6h","6s","6d"):6,("5c","5h","5s","5d"):5,
	("4c","4h","4s","4d"):4,("3c","3h","3s","3d"):3,("2c","2h","2s","2d"):2}
	#print(card)
	for keys in values.keys():
		for key in keys:
			if key in card:
				count += values.get(keys)
	#print(count)
	return count
	
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
	deck = deck[2]
	return cards, dealer, deck, count
	
def deal(cards,dealer,deck):
	cards.append(deck[0])
	deck.pop(0)
	dealer.append(deck[0])
	deck.pop(0)
	cards.append(deck[0])
	deck.pop(0)
	dealer.append(deck[0])
	deck.pop(0)
	count1 = count_cards(cards,count)
	return cards,dealer,deck,count1

def hit(cards,dealer,deck,count):
	cards.append(deck[0])
	deck.pop(0)
	dealer.append(deck[0])
	deck.pop(0)
	count = count_cards(cards,count)
	return cards, dealer, deck, count
	
def bust(count):
	if count > 21:
		print("")
		print("count: " + str(count))
		print("")
		print("BUST")
		print("BUST")
		print("BUST")
		print("BUST")
		print("")
		play_again()
		
def ace(cards, dealer, count):
	### Need to pass in cards and minus by 10 if count >21
	### Need to do the same for dealer
	### Need to implement a dealer_count 
	
def play_again():
	selection = False
	while not selection:
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
	dealer = game[1]
	bust(count)
	ace(cards,dealer)
	#print(game)
	print("Hello " + name + "!")
	print("")
	print("")
	if len(cards) == 2:
		print("Your cards are: " + str(cards[0]) + ", " + str(cards[1]))
	elif len(cards) == 3:
		print("Your cards are: " + str(cards[0]) + ", " + str(cards[1]) + ", " + str(cards[2]))
	elif len(cards)	== 4:
		print("Your cards are: " + str(cards[0]) + ", " + str(cards[1]) + ", " + str(cards[2]) + ", " + str(cards[3]))	
	print("")
	print("Count: " + str(count))
	print("")
	print("---------------------------------")
	print("")
	print("Dealer has: " + str(dealer[0]))
	print("")
	print("---------------------------------")
	print("")
	print("")
	choice = input("Would you like to: \n 1.Hit \n 2.Stay \n\n: ")
	if choice == "1":
		game = hit(game[0],game[1],game[2],game[3])
		menu(name,game)
	if choice == "2":
		print(choice)
		
def blackjack(name):
	cards = []
	dealer = []
	game = draw_game(cards,dealer)
	menu(name,game)
	
name = intro()
blackjack(name)
#Make Ace 11 or 1
#Create logic for dealer staying or hitting.
#Make winning event
