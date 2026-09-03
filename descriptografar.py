from cryptography.fernet import Fernet
import os 

def carregar_chave():
    return open("chave_key", "rb").read()

def descriptografar_arquivos(arquivo,chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_descriptpgrafados  = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptpgrafados)


def encontrar_arquivos(diretorio):   
    lista = []
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
            for nome in arquivos:
                caminho = os.path.join(raiz, nome)
                if nome != "ransoware.py" and not nome.endswith(".key"):
                    lista.append(caminho)
    return lista         


def main():
     chave = carregar_chave()
     arquivos = encontrar_arquivos("test_files")
     for arquivo in arquivos:
        descriptografar_arquivos(arquivo, chave)
     print("Iniciando restauração")
     print("Arquivos restaurados com sucesso")    

if __name__=="__main__":
    main()        