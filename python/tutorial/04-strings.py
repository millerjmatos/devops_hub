x = '''Curso Python,
a cada dia aprenda um pouco mais,
o Python é fascinante, não é mesmo?
Não desista, você está no caminho!!'''
print(x)

print("Print apenas se 'vida' estiver presente:")
txt_in = "As melhores coisas da vida são de graça!"
if "vida" in txt_in:
  print("Sim, 'vida' está presente!")

print("Apenas se 'caro' NÃO estiver presente:")
txt_not_in = "As melhores coisas da vida são de graça!"
if "caro" not in txt_not_in:
  print("'caro' NÃO está presente!")

quantidade = 2
item = 567
valor = 49.95
pedido = "Eu quero {} do item {} que está por R$ {}." # é possível colocar índices dentro dos {}
print(pedido.format(quantidade, item, valor))