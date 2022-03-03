# mover_aleatorio


import os, shutil, random


def remove_dir(lista_dir, more_dir=[]):
    '''Recebe uma lista com diretórios
    e opcionalmente diretórios a serem
    removidos. remove diretórios pre-
    retabelecidos e também outros
    diretórios indesejados.'''
    
    if os.getcwd() == 'C:\\':
        blacklisted = ['$Recycle.Bin', '$WinREAgent', 'Arquivos de Programas', 
                       'Documents and Settings', 'DumpStack.log.tmp', 'hiberfil.sys', 
                       'Intel', 'OneDriveTemp', 'pagefile.sys', 'PerfLogs', 'ProgramData', 
                       'Recovery', 'swapfile.sys', 'System Volume Information', 'Windows']
    else:
        blacklisted = ['.Trash-1000', 'msdownld.tmp', 'SteamLibrary']
    
    blacklisted.append(more_dir)
        
    for i in range(len(blacklisted)):
        lista_dir.remove(blacklisted[i])
        
    return lista_dir


def add_path(path, lista):
    '''Recebe um um caminho e uma lista
    e retorna a lista com o caminho em cada
    item.'''
    
    for i in range(len(lista)):
        lista[i] = os.path.join(path, lista[i])
    
    return lista

def remove_files(lista):
    '''Recebe uma lista e remove os arquivos
    da mesma.'''
    
    only_dir = []
    for item in lista:
        if os.path.isdir(item):
            only_dir.append(item)
        else:
            None

    return only_dir

def subfolder_finder(path):
    '''Recebe um caminho e retorna as suas 
    subpastas.'''
    
    subpastas = os.listdir(path)
    subpastas = add_path(path, subpastas)
    subpastas = remove_files(subpastas)
    
    return subpastas


def rep_pastas(path):
    ''''Recebe um caminho e retorna todas
    as pastas elegíveis para transferência.'''
    os.chdir(path)
    #a primeira leva de pastas tem que passar pela remove_dir
    if path == 'D:' or path == 'C:':
        pastas = remove_dir(os.listdir(path))
    else:
        pastas = os.listdir(path)
    pastas = add_path(path, pastas)
    pastas = remove_files(pastas)
    
    #agora vem o loop
    i = 0
    while i < len(pastas):
        subpastas = subfolder_finder(pastas[i])
        pastas += subpastas
        #print(i, 'de', len(pastas))
        i += 1
    
    return pastas

def move_random(path, folders):
    '''recebe um caminho origem e uma lista de
    destinos, escolhe um destino aleatorio e move
    a pasta origem para este.'''
    
    source = path
    destination = folders[random.randint(0, len(folders))]
    
    shutil.move(source, destination)
    
    with open(os.path.join("D:", "key.txt"), 'w') as file:
        file.write(destination)
    
    shutil.move(os.path.join("D:", "key.txt"), folders[random.randint(0, len(folders))])

def start():
    print("Olá! Seja bem vindo ao transferidor 3000!", end="\n")
    print("Este programa transfere uma pasta ou arquivo para um destino aleatório dentro do HD, e gera uma chave que é posicionada em um lugar também aleatório", end="\n")
    print("")
    
    while True:
        HDD = input("Para começar, digite a letra do HD de destino (C ou D ou G, etc): ") + ":"
        try:
            os.chdir(HDD)
        except FileNotFoundError:
            print("Caminho incorreto, escolha um HD válido!")
        else:
            print("Feito!")
            break
    
    print("")
    origem = input("Agora digite o caminho pasta por pasta da pasta/arquivo que deseja mover (Discos devem ter o seguinte formato: X:\): ")
    caminho = origem
    while caminho != "":
        caminho = input("Digite a proxima pasta (ou dê enter para terminar) " + "[" + origem + "]")
        if caminho == "":
            break
        else:
            origem = os.path.join(origem, caminho)
    print("")
    print("Criando lista de possíveis destinos...")
    destinos = rep_pastas(HDD)
    print("Feito!")
    print("")
    print("Movendo para um destino e criando chave \"key\" para localização...")
    move_random(origem, destinos)
    print("Feito!")
    print("")
    print("Pasta/Arquivo transferido!")
    print("")
    print("Encerrando.")


def start_alternate():
    print("Olá! Seja bem vindo ao transferidor 3000!", end="\n")
    print("Este programa transfere uma pasta ou arquivo para um destino aleatório dentro do HD, e gera uma chave que é posicionada em um lugar também aleatório", end="\n")
    print("")
    
    while True:
        HDD = input("Para começar, digite a letra do HD de destino (C ou D ou G, etc): ") + ":"
        try:
            os.chdir(HDD)
        except FileNotFoundError:
            print("Caminho incorreto, escolha um HD válido!")
        else:
            print("Feito!")
            break
    
    print("")
    origem = input("Agora digite o caminho pasta por pasta da pasta/arquivo que deseja mover (Discos devem ter o seguinte formato: X:\): ")
    caminho = origem
    while caminho != "":
        caminho = input("Digite a proxima pasta (ou dê enter para terminar) " + "[" + origem + "]")
        if caminho == "":
            break
        else:
            origem = os.path.join(origem, caminho)
    print("")
    print("Criando lista de possíveis destinos...")
    destinos = rep_pastas(HDD)
    print("Feito!")
    print("")
    print("Movendo para um destino e criando chave \"key\" para localização...")
    move_random(origem, destinos)
    print("Feito!")
    print("")
    print("Pasta/Arquivo transferido!")
    print("")
    print("Encerrando.")

start_alternate()