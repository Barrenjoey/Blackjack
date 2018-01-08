"""___Blackjack Text-game___
This is a simple BlackJack text-game. The game is designed to express the logic of the blackjack
game and does not offer any gui type interfaces, however it may be added in the future. The aim
was to practice a functional style of programming with functions that could be shared for 
different situations (and players).
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
	for keys in values.keys():
		for key in keys:
			if key in cards:
				count += values.get(keys)
			if key in dealer:
				dealer_count += values.get(keys)
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
	
def bankroll():
	print()
	chips = input("What bankroll would you like to play with? ")
	return chips
	
def place_wager(chips):
	chips = int(chips)
	if chips <= 0:
		play_again()
	print()
	print("---------------------------------")
	print()
	print("Bankroll: " + str(chips))
	selection = False
	while not selection:
		print()
		wager = int(input("Place bet: "))
		if wager <= chips:
			chips -= wager
			return chips, wager
		else:
			print("Invalid Selection. Try Again.")
	
def shuffle():
	d = deck()
	random.shuffle(d)
	return d

def draw_game(cards,dealer):
	deck = shuffle()
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
	count2 = count1[0]
	count3 = count1[1]
	return cards,dealer,deck,count2,count3

def hit(cards,dealer,deck,count,dealer_count):
	cards.append(deck[0])
	deck.pop(0)
	counts = count_cards(cards,count,dealer,dealer_count)
	count = counts[0]
	return cards, dealer, deck, count, dealer_count
		
def ace(cards, dealer, count, dealer_count):
	aces = ["Ac","Ah","As","Ad"]
	for a in aces:
		if a in cards and count > 21:
			count -= 10
		if a in dealer and dealer_count > 21:
			dealer_count -= 10
	return count, dealer_count	

def dealer_turn(count, dealer_count, dealer, deck, cards, chips, wager):
	game = []
	if dealer_count < count:
		game = dealer_hit(dealer,dealer_count, deck, count, cards)
	elif dealer_count == count and dealer_count < 21:
		game = dealer_hit(dealer,dealer_count, deck, count, cards)
	elif dealer_count == 21 and count == 21:
		print("You both have 21.")
		print("It's a push!")
		chips += wager
		blackjack(name,chips)
	else:
		if len(dealer) == 2:
			print()
			print("Dealer turned a: {}".format(dealer[1]))
			print()
			print("Dealer has {0}. You have {1}. You Lose!!".format(dealer_count,count))
			blackjack(name,chips)
		else:
			print()
			print("Dealer has {0}. You have {1}. You Lose!!".format(dealer_count,count))
			blackjack(name,chips)
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
			name = intro()
			chips = bankroll()
			blackjack(name,chips)
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

def menu(name,game,chips,wager):
	os.system('cls')
	cards = game[0]
	count = game[3]
	deck = game[2]
	dealer_count = game[4]
	dealer = game[1]
	aceScore = ace(cards,dealer,count,dealer_count)
	count = aceScore[0]
	dealer_count = aceScore[1]
	dealer_viscount = dealer_visible_count(dealer,dealer_count)
	print()
	print("Hello " + name + "!")
	print()
	print("Bankroll: " + str(chips))
	print()
	print("Wager: " + str(wager))
	print()
	print("---------------------------------")
	print()
	if len(cards) == 2:
		print("Your cards are: " + str(cards[0]) + ", " + str(cards[1]))
	elif len(cards) == 3:
		print("Your cards are: " + str(cards[0]) + ", " + str(cards[1]) + ", " + str(cards[2]))
	elif len(cards)	== 4:
		print("Your cards are: " + str(cards[0]) + ", " + str(cards[1]) + ", " + str(cards[2]) + ", " + str(cards[3]))	
	elif len(cards)	== 5:
		print("Your cards are: " + str(cards[0]) + ", " + str(cards[1]) + ", " + str(cards[2]) + ", " + str(cards[3]) + ", " + str(cards[4]))
	print()
	print("Count: " + str(count))
	print()
	if count > 21:
		print("BUST!")
		print("BUST!")
		print("BUST!")
		blackjack(name,chips)
	print("---------------------------------")
	print()
	if len(dealer) == 2:
		print("Dealer has: " + str(dealer[0]))
	else:
		dealCards = ""
		for i in dealer:
			dealCards += (i + ', ') 
		print("Dealer has: {}".format(dealCards)) 
	print()
	print("Count: " + str(dealer_viscount))
	print()
	print("---------------------------------")
	print()
	if len(dealer) != 2: 
		if dealer_count < 21:
			game = dealer_turn(count, dealer_count, dealer, deck, cards, chips, wager)
			menu(name,game,chips,wager)
		elif dealer_count == 21 and count != 21:
			print()
			print("Dealer has 21. You Lose!")
			blackjack(name,chips)
		elif dealer_count ==21 and count == 21:
			print("You both have 21.")
			print("It's a push!")
			chips += wager
			blackjack(name,chips)
		else:
			print()
			print("Dealer BUSTED!!!")
			print()
			print("YOU WIN!!!!!")
			chips += (wager*2)
			blackjack(name,chips)
	if len(dealer) == 2:		
		choice = input("Would you like to: \n\n 1.Hit \n 2.Stay \n\n: ")
		if choice == "1":
			game = hit(game[0],game[1],game[2],game[3],game[4])
			menu(name,game,chips,wager)
		elif choice == "2":
			game = dealer_turn(count, dealer_count, dealer, deck, cards, chips, wager)
			menu(name,game,chips,wager)
	
def blackjack(name,chips):
	cards = []
	dealer = []
	game = draw_game(cards,dealer)
	wager = place_wager(chips)
	menu(name,game,wager[0],wager[1])

name = intro()
chips = bankroll()
blackjack(name,chips)

#Add split/double down etc
#Add blackjack payout
