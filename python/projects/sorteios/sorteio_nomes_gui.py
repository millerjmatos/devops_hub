import random
import tkinter as tk
from tkinter import Entry, Button, Text, Scrollbar

def ler_arquivo(arquivo):
    with open(arquivo, 'r') as file:
        nomes = file.readlines()
    return [nome.strip() for nome in nomes]

def gerar_nomes(quantidade):
    nomes = ler_arquivo('nome.txt')
    sobrenomes = ler_arquivo('sobrenome.txt')

    sobrenomes_unicos = list(set(sobrenomes))

    if len(sobrenomes_unicos) < 2:
        return ["É necessário ter pelo menos dois sobrenomes únicos."]
    else:
        resultados = []
        for _ in range(quantidade):
            nome_aleatorio = random.choice(nomes)
            sobrenome_aleatorio1 = random.choice(sobrenomes_unicos)
            sobrenome_aleatorio2 = random.choice(sobrenomes_unicos)

            nome_completo = f'{nome_aleatorio} {sobrenome_aleatorio1} {sobrenome_aleatorio2}'
            resultados.append(nome_completo)
        return resultados

def gerar_nomes_callback():
    quantidade = int(entry_quantidade.get())
    resultados = gerar_nomes(quantidade)
    resultado_text.config(state=tk.NORMAL)  # Habilitar edição do Text
    resultado_text.delete('1.0', tk.END)   # Limpar o conteúdo atual
    resultado_text.insert(tk.END, "\n".join(resultados))  # Inserir os novos resultados
    resultado_text.config(state=tk.DISABLED)  # Desabilitar edição do Text

root = tk.Tk()
root.title("Gerador de Nomes Aleatórios")

label_quantidade = tk.Label(root, text="Quantidade de Nomes:")
label_quantidade.pack()

entry_quantidade = Entry(root)
entry_quantidade.pack()

button_gerar = Button(root, text="Gerar Nomes", command=gerar_nomes_callback)
button_gerar.pack()

# Utilizando o widget Text para exibir os resultados
resultado_text = Text(root, wrap=tk.WORD, height=10, width=40)
resultado_text.pack()

# Adicionando uma barra de rolagem vertical
scrollbar = Scrollbar(root, command=resultado_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
resultado_text.config(yscrollcommand=scrollbar.set)

# Desabilitando a edição direta no widget Text
resultado_text.config(state=tk.DISABLED)

root.mainloop()
