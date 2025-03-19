import os
import shutil
import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# Lista de caminhos de origem e destino
pastas_para_mover = [
    {"origem": r"T:\caminho\caminho\caminho", "destino": r"T:\caminho\caminho\caminho\caminho"},
    {"origem": r"T:\caminho\caminho\caminho", "destino": r"T:\caminho\caminho\caminho\caminho"},
    {"origem": r"T:\caminho\caminho\caminho", "destino": r"T:\caminho\caminho\caminho\caminho"},
    {"origem": r"T:\caminho\caminho\caminho", "destino": r"T:\caminho\caminho\caminho\caminho"},
    {"origem": r"T:\caminho\caminho\caminho", "destino": r"T:\caminho\caminho\caminho\caminho"},
]

# Função para obter as datas corretas
def obter_datas_para_busca():
    hoje = datetime.date.today()
    if hoje.weekday() == 0:  # Segunda-feira
        datas = [(hoje - datetime.timedelta(days=i)).strftime("%Y%m%d") for i in range(2, -1, -1)]
    else:
        datas = [hoje.strftime("%Y%m%d")]
    return datas

# Função que copia as pastas e atualiza a interface
def copiar_pastas():
    datas_validas = obter_datas_para_busca()
    total_pastas = len(pastas_para_mover)
    progresso["maximum"] = total_pastas

    resultado_texto = ""
    for i, item in enumerate(pastas_para_mover):
        origem = item["origem"]
        destino = item["destino"]

        for pasta in os.listdir(origem):
            if pasta in datas_validas:
                caminho_pasta = os.path.join(origem, pasta)
                destino_pasta = os.path.join(destino, pasta)

                if os.path.isdir(caminho_pasta):  
                    if os.path.exists(destino_pasta):  
                        resultado_texto += f"Pasta '{pasta}' já existe no destino, não foi copiada.\n"
                    elif not os.listdir(caminho_pasta):  
                        resultado_texto += f"Pasta '{pasta}' está vazia, não foi copiada.\n"
                    else:
                        shutil.copytree(caminho_pasta, destino_pasta)  
                        resultado_texto += f"Pasta '{pasta}' copiada com sucesso!\n"

        progresso["value"] = i + 1
        root.update_idletasks()

    messagebox.showinfo("Processo Concluído", resultado_texto)

# Criar interface Tkinter
root = tk.Tk()
root.title("Copiador de Pastas")
root.geometry("400x200")

label = tk.Label(root, text="Copiando pastas...", font=("Arial", 12))
label.pack(pady=10)

progresso = ttk.Progressbar(root, length=300, mode="determinate")
progresso.pack(pady=10)

botao = tk.Button(root, text="Iniciar Cópia", command=copiar_pastas)
botao.pack(pady=20)

root.mainloop()
