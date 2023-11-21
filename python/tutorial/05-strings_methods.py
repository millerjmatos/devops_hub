# Todos os métodos de strings retornam novos valores, mas NÃO mudam a string original.

a = "python, é minha linguagem favorita!"
b = "PYTHON NÃO É DIFÍCIL"
print(a.upper())
print(b.lower())

txt_a = "  Esta é uma string   "
resultado = txt_a.strip()
print(resultado)  # Saída: "Esta é uma string"

txt_b = "maçã banana cereja"
palavras = txt_b.split()
print(palavras)  # Saída: ['maçã', 'banana', 'cereja']

palavras = ['maçã', 'banana', 'cereja']
txt_c = ', '.join(palavras)
print(txt_c)  # Saída: "maçã, banana, cereja"

txt_d = "A noite estava estrelada e a lua estava cheia."
novo_texto = txt_d.replace("a lua estava cheia", "o céu estava lindo")
print(novo_texto)

txt_e = "Olá, mundo!"
comeca_com_ola = txt_e.startswith("Ola")
termina_com_mundo = txt_e.endswith("mundo!")