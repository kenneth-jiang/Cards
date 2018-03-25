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
	def __init__(self):
		suits = ("Hearts", "Diamonds", "Clubs", "Spades")
		values =  ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
		self.cards = [Card(value, suit) for suit in suits for value in values]

	def count(self):
		return len(self.cards)

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def _deal(self, num):
		count = self.count()
		if count == 0:
			raise ValueError("All cards have been dealt")
		actual = min(count, num)
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards

	def shuffle(self):
		if num_cards == 52:

		else:
			raise ValueError("Only full decks can be shuffled")

	def deal_card(self):
		pass

	def deal_hand(self, num):
		pass