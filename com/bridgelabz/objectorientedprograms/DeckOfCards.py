from com.bridgelabz.utility.Oops_Utility import DeckOfCards

if __name__ == '__main__':
    deckofcards_obj=DeckOfCards()
    suffled_cards=deckofcards_obj.deckOfCardsLogic()
    deckofcards_obj.print2DdeckofCards(suffled_cards)