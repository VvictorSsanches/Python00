'''
from math import sqrt, floor
num = int(input('digite um número: '))
raiz = sqrt(num)
print('A raiz de um {} é igual a {:.2f}'.format(num, floor(raiz)))
'''
import random
num = random.randint(1, 10)
print(num)

import emoji
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
#Python is 👍
print(emoji.emojize('Python is :thumbs_up:', language='alias'))
#Python is 👍
print(emoji.demojize('Python is 👍'))
#Python is :thumbs_up:
print(emoji.emojize("Python is fun :red_heart:"))
#Python is fun ❤
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
#Python is fun ❤️ #red heart, not black heart
print(emoji.is_emoji("👍"))
True
print(emoji.emojize('python is dragon :dragon:'))

print(emoji.emojize('Você ganhou um :globe_showing_Americas:'))
