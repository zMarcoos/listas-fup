from random import randint

cards = []
types = ['Ás', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
suits = ['paus', 'ouros', 'copas', 'espadas']

for suit in suits:
  for type in types:
    cards.append(f'{type} de {suit}')
        
for index in range(4):
  print(f'Jogador {index + 1}: ', end='')

  for _ in range(5):
    card = cards[randint(0, len(cards) - 1)]

    print(card, end=' | ')
    cards.remove(card)
      
  print('')