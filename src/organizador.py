import shutil
import os
import ujson
import glob
import time
import platform

def configurar(arquivo="./config.json"):
    with open(arquivo) as arquivo:
        config = ujson.load(arquivo)
        return config["config"]

def mover():
    sistema = platform.system().lower()
    usuario = os.getlogin()
    config = configurar()
    caminho_telegram = config[sistema]["origem"].format(usuario)
    caminho_arquivos = config[sistema]["mover"].format(usuario)
    formatos_arquivos = config["formatos"]
    for formato in formatos_arquivos:
        formato = "*." + formato
        arquivos = glob.glob1(caminho_telegram, formato)
        lista_arquivos = []
        for arquivo in arquivos:
            diretorio = caminho_telegram + "/" + arquivo
            shutil.move(diretorio, caminho_arquivos)
            lista_arquivos.append(arquivo)
            print("O arquivo {0} foi movido".format(arquivo))
            time.sleep(1)

if __name__ == '__main__':
    mover()
