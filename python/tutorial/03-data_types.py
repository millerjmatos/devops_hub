pais = "Brasil"
quantidade = 5
print(pais, "ganhou", quantidade, "títulos mundiais!!")

###

x_str = str(3)    # x_str será '3'

y_int = int(3)    # y_int será 3

z_float = float(3)  # z_float será 3.0

a_list = ["maçã", "banana", "uva"]

print(type(x_str))

print(type(y_int))

print(type(z_float))

print(type(pais))

print(type(quantidade))

print(type(a_list))

###

import random

print(random.randrange(0,101)) # do 1 ao 100

print(random.choice(['Muller', 'Gabi', 'João', 'Maria']))

print(random.sample([1, 5, 9, 11, 12, 22, 25, 26], k=4)) # sorteia 4 items