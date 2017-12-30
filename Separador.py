#Separador_De_Arquivos

import shutil
import glob
import time
import os

def getMusicas():
    i = 0
    
    mv = glob.glob1(r'C:\Users\SEU_USER\Downloads\Telegram Desktop','*.MP3')
    lc = r'C:\Users\SEU_USER\Downloads\Telegram Desktop\Musicas'

    try:
        os.mkdir(r'C:\Users\SEU_USER\Downloads\Telegram Desktop\Musicas')
    except OSError:
        print('A pasta Musicas ja foi criada!')
    
    while(i<= len(mv)):
        shutil.move(mv[i],lc)
        print(mv[i])
        time.sleep(1)
        i = i + 1

getMusicas()

