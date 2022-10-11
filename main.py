"""
Title: Blackjack Easy
Author: Michał Chojna
Date: 10.06.2022
Description: Calculator to add, subtract, multiply and divide
"""

# Imports modules
import art
import random
import os


def card_deal(hand, cards):
    hand.append(random.choice(cards))


def another_card():
    check = True
    while check and sum(player_hand) < 21:
        another = input("Type 'yes' to get another card, type 'no' to pass: ")
        if another.lower() == 'yes' or another.lower() == 'no':
            return another


def ace_check(hand):
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)


check = True
while check:
    blackjack = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")
    if blackjack.lower() == 'yes' or blackjack.lower() == 'no':
        break

while blackjack.lower() == 'yes':

    os.system("clear")

    print(art.logo)

    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player_hand = []
    dealer_hand = []

    for num in range(2):
        card_deal(player_hand, deck)
        card_deal(dealer_hand, deck)

    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Dealer's cards: [{dealer_hand[0]}, X], current score: {dealer_hand[0]}")

    game = another_card()

    while game.lower() == "yes":

        card_deal(player_hand, deck)
        ace_check(dealer_hand)

        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"Dealer's cards: [{dealer_hand[0]}, X], current score: {dealer_hand[0]}")

        if sum(player_hand) < 21:
            game = another_card()
        elif sum(player_hand) == 21:
            game = "no"
        else:
            print("You went over. Dealer wins!")
            game = "no"

    while sum(player_hand) <= 21 and sum(dealer_hand) < 21:
        if sum(dealer_hand) < 17 or sum(dealer_hand) < sum(player_hand):
            card_deal(dealer_hand, deck)

            ace_check(dealer_hand)

            print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
            print(f"Dealer's cards: [{dealer_hand}, current score: {sum(dealer_hand)}")

        else:
            print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
            print(f"Dealer's cards: [{dealer_hand}, current score: {sum(dealer_hand)}")
            break

    if sum(player_hand) <= 21:
        if sum(dealer_hand) > 21:
            print("Dealer went over. You win!")
        elif sum(dealer_hand) == sum(player_hand):
            print("Draw!")
        elif sum(dealer_hand) < sum(player_hand):
            print("Dealer wins!")
        elif sum(dealer_hand) > sum(player_hand):
            print("You win!")

    check = True
    while check:
        blackjack = input("Do you want to play another game of Blackjack? Type 'yes' or 'no': ")
        if blackjack.lower() == 'yes':
            os.system("clear")
            break
        elif blackjack.lower() == 'no':
            break
