# está abrindo o arquivo existente no modo 'reading'

f = open("demofile.txt", "r")
print(f.read())

###

f2 = open("demofile2.txt", "a")
f2.write("\nAgora tem mais coisa aqui!!")
f2.close()

###

f3 = open("demofile3.txt", "w")
f3.write("Deletei tudo!!!")
f3.close()

f3 = open("demofile3.txt", "r")
print(f3.read())

###

# "x" criará um arquivo, mas retornará um erro se o arquivo já existir.

# "w" criará um arquivo se o arquivo especificado não existir e permitirá que você escreva dados no arquivo, substituindo o conteúdo existente, se houver.

data = open("welcome.txt", "x")

###

import os
os.remove("welcome.txt") # deleta o arquivo