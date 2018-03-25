class Card:
	def __init__(self, suit, value):
		if suit in ("Hearts", "Diamonds", "Clubs", or "Spades"):
			self.suit = suit
		else:
			raise ValueError("Suit must be Hearts, Diamonds, Clubs, or Spades")
		if value in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"):
			self.value = value
	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:
	pass