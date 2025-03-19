import os
import shutil

# Caminho onde a pasta Consolidado pode estar
origem = os.path.expanduser("C:~pasta")

# Caminho de destino na rede (ajuste conforme necessário)
destino = "C:\\caminho"  # Exemplo para Windows

# Lista todas as pastas que começam com "Consolidado_"
for pasta in os.listdir(origem):
    if pasta.startswith("Consolidado_"):  # Verifica se o nome começa com "Consolidado_"
        caminho_pasta = os.path.join(origem, pasta)  # Cria o caminho completo da pasta

        if os.path.isdir(caminho_pasta):  # Confirma se é uma pasta
            if os.listdir(caminho_pasta):  # Verifica se a pasta tem arquivos dentro
                shutil.move(caminho_pasta, os.path.join(destino, pasta))  # Move a pasta para a rede
                print(f"Pasta '{pasta}' movida com sucesso!")
            else:
                print(f"A pasta '{pasta}' está vazia, não será movida.")
