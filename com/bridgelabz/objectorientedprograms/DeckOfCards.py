"""
purpose   :  To create Deck Of Cards.Shuffle the cards using Random method and then distribute
             9 Cards to 4 Players and Print the Cards the received by the 4 Players
             using 2D Array
@Author   : Rohini Zade
@version  : 1.0
@since    : 5-12-2018

"""
from com.bridgelabz.utility.Oops_Utility import DeckOfCards

if __name__ == '__main__':
    deckofcards_obj=DeckOfCards()
    suffled_cards=deckofcards_obj.deckOfCardsLogic()
    deckofcards_obj.print2DdeckofCards(suffled_cards)