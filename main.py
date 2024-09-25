import tkinter as tk
from tkinter import messagebox

# Função que será chamada ao clicar no botão
def submit():
    nome_completo = entry_nome.get()
    numero_telefone = entry_telefone.get()
    senha = entry_senha.get()

    # Verifica se todos os campos foram preenchidos
    if nome_completo and numero_telefone and senha:
        # Aqui você pode adicionar o código para salvar ou enviar os dados
        messagebox.showinfo("Informação", "Dados enviados com sucesso!")
        print(f"Nome Completo: {nome_completo}")
        print(f"Número de Telefone: {numero_telefone}")
        print(f"Senha: {senha}")
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")

# Criação da janela principal
root = tk.Tk()
root.title("Automatizador de Dados")

# Nome completo
tk.Label(root, text="Nome Completo:").grid(row=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

# Número de telefone
tk.Label(root, text="Número de Telefone:").grid(row=1)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=1, column=1)

# Senha
tk.Label(root, text="Senha:").grid(row=2)
entry_senha = tk.Entry(root, show="")  # 'show=""' oculta a senha
entry_senha.grid(row=2, column=1)

# Botão para enviar os dados
submit_button = tk.Button(root, text="Enviar", command=submit)
submit_button.grid(row=3, column=1)

# Inicia o loop principal da interface
root.mainloop()