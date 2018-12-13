"""
purpose   : To create a Player Object having Deck of Cards, and having ability to Sort by Rank
            and maintain the cards in a Queue implemented using Linked List. Do not use any
            Collection Library. Further the Player are also arranged in Queue. Finally Print
            the Player and the Cards received by each Player.


@Author   : Rohini Zade
@version  : 1.0
@since    : 5-12-2018
"""

from com.bridgelabz.utility.Oops_Utility import DeckOfCards, SortedDeckOfCards
from com.bridgelabz.utility.Datastructure_utility import QueeByLinklist

if __name__ == '__main__':
    q_linklist_obj = QueeByLinklist()
    deckofcards_obj=DeckOfCards()
    cards=deckofcards_obj.sortedDeckOfCardsLogic()


    player1 = SortedDeckOfCards(cards[:9])
    print("cards of player 1:")
    cardslist = player1.rankCards()
    print(cardslist)
    print("\n")

    # player2 = SortedDeckOfCards(cards[9:18])
    # print("cards of player 2:")
    # cardslist.clear()
    # cardslist = player2.rankCards()
    # print(cardslist)
    # print("\n")
    #
    # player3 = SortedDeckOfCards(cards[18:27])
    # cardslist.clear()
    # print("cards of player 3:")
    # cardslist = player3.rankCards()
    # print(cardslist)
    # print("\n")
    #
    # player4 = SortedDeckOfCards(cards[27:36])
    # cardslist.clear()
    # print("cards of player 4:")
    # cardslist=player4.rankCards()
    # print(cardslist)
    #



