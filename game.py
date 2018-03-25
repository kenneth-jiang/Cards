class Card:
	def __init__(self, suit, value):
		if suit in ("Hearts", "Diamonds", "Clubs", "Spades"):
			self.suit = suit
		else:
			raise ValueError("Suit must be Hearts, Diamonds, Clubs, or Spades")
		if value in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"):
			self.value = value
		else:
			raise ValueError("Value must be A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K")
	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:
	num_cards = 0
	def __init__(self):
		for suit in ("Hearts", "Diamonds", "Clubs", "Spades"):
			for value in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"):
				Card(suit, value)
				Deck.num_cards += 1
	def count(self):
		return Deck.num_cards
	def __repr__(self):
		return f"Deck of {num_cards} cards"
	def _deal(self, num):
		if num <= num_cards:
			num_cards -= num
		else:
			num_cards = 0
		if num_cards == 0:
			raise ValueError("All cards have been dealt")
	def shuffle(self):
		if num_cards == 52:

		else:
			raise ValueError("Only full decks can be shuffled")
			