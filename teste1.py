import tkinter as tk
from tkinter import messagebox
import random

# Configurações iniciais
disponiveis = list(range(1, 76))
historico = []

# Cores do sistema
AZUL = "#061B50"
AZUL_CLARO = "#102F75"
DOURADO = "#FFC000"
BRANCO = "#FFFFFF"
PRETO = "#111111"
VERDE = "#168A27"

# Janela principal
janela = tk.Tk()
janela.title("Máfia da Sorte - Bingo")
janela.geometry("1080x720")
janela.configure(bg=AZUL)
janela.resizable(True, True)

# Cabeçalho
cabecalho = tk.Frame(janela, bg=AZUL, pady=15)
cabecalho.pack(fill="x")

titulo = tk.Label(
    cabecalho,
    text="🎩 MÁFIA DA SORTE 🍀",
    font=("Arial", 30, "bold"),
    fg=DOURADO,
    bg=AZUL
)
titulo.pack()

subtitulo = tk.Label(
    cabecalho,
    text="BINGO DA SORTE • SORTEIO DE 1 A 75",
    font=("Arial", 12, "bold"),
    fg=BRANCO,
    bg=AZUL
)
subtitulo.pack(pady=5)

# Linha decorativa
tk.Frame(
    janela,
    bg=DOURADO,
    height=3
).pack(fill="x", padx=30, pady=5)

# Área principal
principal = tk.Frame(janela, bg=AZUL)
principal.pack(fill="both", expand=True, padx=25, pady=15)

# Painel esquerdo
painel_esquerdo = tk.Frame(
    principal,
    bg=AZUL_CLARO,
    padx=20,
    pady=20
)
painel_esquerdo.pack(side="left", fill="both", expand=True, padx=10)

tk.Label(
    painel_esquerdo,
    text="NÚMERO SORTEADO",
    font=("Arial", 16, "bold"),
    fg=DOURADO,
    bg=AZUL_CLARO
).pack(pady=10)

# Bola do sorteio
bola = tk.Label(
    painel_esquerdo,
    text="--",
    font=("Arial", 65, "bold"),
    fg=PRETO,
    bg=BRANCO,
    width=3,
    height=1,
    relief="raised",
    bd=5
)
bola.pack(pady=15)

# Informação do sorteio
informacao = tk.Label(
    painel_esquerdo,
    text="Aguardando sorteio...",
    font=("Arial", 12),
    fg=BRANCO,
    bg=AZUL_CLARO
)
informacao.pack(pady=10)

# Botão sortear
def sortear():
    global disponiveis

    if not disponiveis:
        messagebox.showinfo(
            "Bingo",
            "Todos os números já foram sorteados!"
        )
        return

    numero = random.choice(disponiveis)
    disponiveis.remove(numero)
    historico.append(numero)

    bola.config(text=str(numero))

    informacao.config(
        text=f"Número {numero} sorteado!"
    )

    # Atualiza histórico
    lista_historico.insert(
        0,
        f"   Número: {numero}"
    )

    # Atualiza quantidade
    quantidade.config(
        text=f"Números sorteados: {len(historico)} / 75"
    )

    # Destaca número no painel
    botoes[numero].config(
        bg=DOURADO,
        fg=PRETO,
        activebackground=DOURADO
    )

    # Atualiza histórico crescente
    crescente.config(
        text="Ordem crescente: " +
        str(sorted(historico))
    )

botao_sortear = tk.Button(
    painel_esquerdo,
    text="🎱  SORTEAR NÚMERO",
    font=("Arial", 16, "bold"),
    bg=DOURADO,
    fg=PRETO,
    activebackground="#E6A800",
    cursor="hand2",
    relief="raised",
    bd=4,
    command=sortear
)
botao_sortear.pack(fill="x", pady=20)

quantidade = tk.Label(
    painel_esquerdo,
    text="Números sorteados: 0 / 75",
    font=("Arial", 12, "bold"),
    fg=DOURADO,
    bg=AZUL_CLARO
)
quantidade.pack(pady=5)

# Painel direito - Histórico
painel_direito = tk.Frame(
    principal,
    bg=AZUL_CLARO,
    padx=15,
    pady=15
)
painel_direito.pack(side="right", fill="both", padx=10)

tk.Label(
    painel_direito,
    text="📋 HISTÓRICO",
    font=("Arial", 16, "bold"),
    fg=DOURADO,
    bg=AZUL_CLARO
).pack(pady=10)

lista_historico = tk.Listbox(
    painel_direito,
    width=25,
    height=16,
    font=("Arial", 12, "bold"),
    bg=BRANCO,
    fg=PRETO,
    selectbackground=DOURADO
)
lista_historico.pack(pady=5)

# Histórico crescente
crescente = tk.Label(
    painel_direito,
    text="Ordem crescente: []",
    font=("Arial", 9),
    fg=BRANCO,
    bg=AZUL_CLARO,
    wraplength=230,
    justify="left"
)
crescente.pack(pady=10)

# Painel dos números
painel_numeros = tk.Frame(
    janela,
    bg=AZUL,
    padx=20,
    pady=5
)
painel_numeros.pack(fill="x")

tk.Label(
    painel_numeros,
    text="PAINEL DE NÚMEROS",
    font=("Arial", 16, "bold"),
    fg=DOURADO,
    bg=AZUL
).pack()

grade = tk.Frame(painel_numeros, bg=AZUL)
grade.pack()

botoes = {}

for numero in range(1, 76):

    botao = tk.Label(
        grade,
        text=str(numero),
        font=("Arial", 10, "bold"),
        fg=PRETO,
        bg=BRANCO,
        width=4,
        height=1,
        relief="raised",
        bd=2
    )

    linha = (numero - 1) // 15
    coluna = (numero - 1) % 15

    botao.grid(
        row=linha,
        column=coluna,
        padx=3,
        pady=3
    )

    botoes[numero] = botao

# Reiniciar bingo
def reiniciar():

    global disponiveis, historico

    resposta = messagebox.askyesno(
        "Reiniciar",
        "Deseja reiniciar o bingo?"
    )

    if resposta:
        disponiveis = list(range(1, 76))
        historico = []

        bola.config(text="--")

        informacao.config(
            text="Aguardando sorteio..."
        )

        quantidade.config(
            text="Números sorteados: 0 / 75"
        )

        lista_historico.delete(0, tk.END)

        crescente.config(
            text="Ordem crescente: []"
        )

        for numero in range(1, 76):
            botoes[numero].config(
                bg=BRANCO,
                fg=PRETO
            )

# Rodapé
rodape = tk.Frame(janela, bg=AZUL)
rodape.pack(fill="x", pady=8)

tk.Button(
    rodape,
    text="🔄 REINICIAR BINGO",
    font=("Arial", 11, "bold"),
    bg=VERDE,
    fg=BRANCO,
    cursor="hand2",
    command=reiniciar
).pack(side="left", padx=30)

tk.Label(
    rodape,
    text="MÁFIA DA SORTE 🍀",
    font=("Arial", 11, "bold"),
    fg=DOURADO,
    bg=AZUL
).pack(side="right", padx=30)

# Atalho para sortear usando ENTER
janela.bind("<Return>", lambda evento: sortear())

# Executar sistema
janela.mainloop()