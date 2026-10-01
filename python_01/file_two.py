# módulo a ser importado em Python
import file_one

print("Estou no file-two")
print(f"__name__ no arquivo dois está definido como: {__name__}")

if __name__ == "__main__":
   print("Arquivo dois executado quando rodou diretamente")
else:
   print("Arquivo dois executado ao ser importado")