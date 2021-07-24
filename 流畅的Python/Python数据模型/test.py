import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds clubs hearts'.split()

result = [Card(rank, suit) for suit in suits
          for rank in ranks]
print(result)
