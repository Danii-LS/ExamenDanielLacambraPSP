from multiprocessing import Pool
from pathlib import Path
import os, time, random

def sizeFile(fichero):
    file_stats = os.stat(fichero)
    print(file_stats)
    print(f' File size in Bytes is {file_stats.st_size}')
    print(f' File size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')


def main():
    #numberThreads = input("Número de threads a usar:")
    #numberThreads = int(numberThreads)

    path1 = Path('fichero1ParaEj2.txt')
    path2 = Path('fichero2ParaEj2.txt')
    
    dirs1 = os.listdir(path1)
    dirs2 = os.listdir(path2)

    listadirs = [dirs1, dirs2]
    for i in range(2):
        sizeFile(listadirs[i])
    

    #pool = Pool(processes=numberThreads)
    #size = pool.map(os.path.getsize, listaFicheros)
    #print(size)
    #pool.close()
    #pool.join()






if __name__ == '__main__':
    main()

    