def my_function_daew():
  print("Fala seus doido!!")
my_function_daew()

###

def get_name():
  return "Muller Matos"

print("Você é " + get_name())

###

def myFunction():
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

###

def _multiplicacao(x):
  return 5.5 * x

print(_multiplicacao(3.5))
print(_multiplicacao(5))
print(_multiplicacao(999))

###

def saudacao(nome):
  print("Olá, " + nome + "!")

saudacao("Gabi")

###

def saudacao_2():
    nome = input("Digite seu nome: ")
    mensagem = f"Olá, {nome}!"
    return mensagem

resultado = saudacao_2()
print(resultado)

###

lista = [1, 2, 3, 4, 5]
comprimento = len(lista)
print(comprimento)  # Saída: 5

y = "Hello, World!"
print(len(y))

###

def soma(a, b):
  return a + b

s = soma(3, 4) # capturando o retorno
print(s)