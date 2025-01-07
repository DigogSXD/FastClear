import os
import shutil
import tempfile
import tkinter as tk
from tkinter import messagebox
import subprocess

# Função para limpar arquivos temporários
def limpar_temporarios():
    temp_dir = tempfile.gettempdir()
    try:
        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        messagebox.showinfo("Sucesso", "Arquivos temporários limpos com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao limpar arquivos temporários: {e}")

# Função para limpar cache do navegador (apenas um exemplo para o Chrome)
def limpar_cache_navegador():
    cache_chrome = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\Default\Cache"
    try:
        if os.path.exists(cache_chrome):
            shutil.rmtree(cache_chrome)
        messagebox.showinfo("Sucesso", "Cache do Chrome limpo com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao limpar cache do Chrome: {e}")

# Função para executar o comando sfc /scannow
def executar_sfc():
    try:
        # Executa o comando sfc /scannow no prompt de comando
        result = subprocess.run(["sfc", "/scannow"], capture_output=True, text=True, check=True)
        # Exibe a saída do comando
        messagebox.showinfo("Resultado do SCAN", f"Saída do comando SFC:\n\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar o SCAN:\n{e.stderr}")

# Função para criar a interface gráfica
def criar_menu():
    # Criando a janela principal com fundo preto
    root = tk.Tk()
    root.title("Menu de Limpeza de PC")
    root.geometry("300x250")  # Tamanho da janela
    root.config(bg="black")  # Definindo fundo da janela como preto

    # Adicionando um título (texto branco)
    label = tk.Label(root, text="Escolha uma opção de limpeza", font=("Arial", 12), fg="white", bg="black")
    label.pack(pady=10)

    # Botões para cada função de limpeza com fundo preto e texto branco
    btn_temporarios = tk.Button(root, text="Limpar Arquivos Temporários", width=25, command=limpar_temporarios, bg="black", fg="white")
    btn_temporarios.pack(pady=5)

    btn_cache = tk.Button(root, text="Limpar Cache do Navegador", width=25, command=limpar_cache_navegador, bg="black", fg="white")
    btn_cache.pack(pady=5)

    btn_scannow = tk.Button(root, text="Executar SCAN", width=25, command=executar_sfc, bg="black", fg="white")
    btn_scannow.pack(pady=5)

    btn_sair = tk.Button(root, text="Sair", width=25, command=root.quit, bg="black", fg="white")
    btn_sair.pack(pady=10)

    # Inicia a interface gráfica
    root.mainloop()

# Função principal
if __name__ == "__main__":
    criar_menu()
