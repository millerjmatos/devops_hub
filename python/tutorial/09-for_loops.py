for x in range(6):
  print(x)

for x in range(2, 5):
  print(x)

for x in range(10, 30, 3): # padrão de incremento é um, mas pode ser alterado
  print(x)

for rodada in range(11,15): # podemos informar os valores manualmente [1,5,6,8...]
  print(rodada)
else:
  print("Acabouu, aee!!")

for i in range(1,8):
    if(i == 5): # pulamos o 5
        continue
    print(i)