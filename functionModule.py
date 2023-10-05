import os, shutil, concurrent.futures, main

global continueMainLoop
errorText, negritaText, inputText, resetText, colorCeleste, continueMainLoop = '\033[91;4m', '\033[1m', '\033[1;33m', '\033[0m', '\033[1;36m', True

commands = [
    ['help', f'Mostrar la descripción de comandos disponibles junto a un ejemplo de uso. ________ {inputText}"help"{resetText}'],
    ['path', f'Cambiar el directorio al especificado indicado por parámetro. ____________________ {inputText}"path C:/Windows"{resetText}'],
    ['back', f'Retroceder al directorio raís del directorio actual o current working directory. _ {inputText}"back"{resetText}'],
    ['copy', f'Copiar el directorio o archivo indicado a una dirección especificada. ____________ {inputText}"copy"{resetText}'],
    ['move', f'Mover un archivo o directorio ingresado a otra dirección. ________________________ {inputText}"move .../archivo .../carpeta"{resetText}'],
    ['rename', f'Cambiar el nombre de un archivo o directorio. __________________________________ {inputText}"rename C:/ProgramFiles/Firefox Chrome"{resetText}'],
    ['create', f'Crear un nuevo archivo o directorio indicando tipo y nombre. ___________________ {inputText}"create file imagen.jpg"{resetText}'],
    ['search', f'Buscar archivos o directorios por nombre en el directorio actual. ______________ {inputText}"search filtro de busqueda"{resetText}'],
    ['delete', f'Borrar un archivo o directorio indicado. _______________________________________ {inputText}"delete C:/Users/Public/Desktop/carpeta"{resetText}'],
    ['exit', f'Salir del programa. ______________________________________________________________ {inputText}"exit"{resetText}']
]


def showDirectoryContent(itemsList, upperMesseage, simpleView):
    print(upperMesseage)
    try:
        for i, item in enumerate(itemsList):
            if os.path.isdir(item):
                print([f'    {i} - {colorCeleste}[dir]{resetText} {(item.split(os.sep))[-1]}' if simpleView else f'    {i} - {colorCeleste}[dir]{resetText} {item}'][0])
            else:
                print([f'    {i} - {inputText}[file]{resetText} {(item.split(os.sep))[-1]}' if simpleView else f'    {i} - {inputText}[file]{resetText} {item}'][0])
    except:
        input(f'{errorText} Acceso denegado a directorio. Pruebe aumentando los permisos con los que el programa corre . . . {resetText}')


def takeUserInput(contextList):
    returnInput = str(input(f'{inputText}\n >> {resetText}'))
    if returnInput is not None:
        
        returnInput = returnInput.split(' ')
        if returnInput[0] not in [item[0] for item in commands]:
            try:
                int(returnInput[0])
            except:
                input(f'{errorText}"{returnInput[0]}" no se reconoce como un comando interno o externo, programa o archivo por lotes ejecutable . . . {resetText}')
                return None
            if int(returnInput[0]) < 0 or int(returnInput[0]) > (len(contextList)) - 1:
                input(f'{errorText}Número de índice ingresado fuera de rango en el contexto de contexto de lista actual . . . {resetText}')
                return None
            else:
                return returnInput
        else:
            return returnInput
        
    else:
        return None


def detectCommand(userCommand, isSearching, contextoDeLista):
    if userCommand is not None:
        
        try:
            int(userCommand[0])
        except:
            if isSearching:
                if userCommand[0] == 'search' or userCommand[0] == 'path' or userCommand[0] == 'create' or userCommand[0] == 'back' or userCommand[0] == 'exit':
                    if userCommand[0] == 'exit':
                        main.main.searching = None
                        return None
                    else:
                        input(f'{errorText}El comando ingresado no tiene un resultado o acción válida en el contexto de listado actual . . . {resetText}')
                        return None
                else:
                    exec(f'{userCommand[0]}({userCommand})')
                    return None
            else:
                if userCommand[0] == 'search':
                    return userCommand
                else:
                    exec(f'{userCommand[0]}({userCommand})')
                    return None
        indexAccess(userCommand, contextoDeLista)
        
    else:
        return None


def indexAccess(userCommand, contextoDeLista, functionCalled=None):
    if functionCalled is not None:
        if int(userCommand) < 0 or int(userCommand) > (len(contextoDeLista)) - 1:
            input(f'{errorText} No se logró otorgar path a partir de acceso desde función . . . {resetText}')
            return None
        else:
            return contextoDeLista[int(userCommand)]
        
    else:
        if os.path.isfile(contextoDeLista[int(userCommand[0])]):
            try:
                os.startfile(contextoDeLista[int(userCommand[0])])
            except:
                input(f'{errorText} No se logró ejecutar el programa seleccionado . . . {resetText}')
        else:
            try:
                os.chdir(contextoDeLista[int(userCommand[0])])
            except:
                input(f'{errorText} Acceso denegado a directorio. Pruebe aumentando los permisos con los que el programa corre . . . {resetText}')



def help(userCommand, optionalParameter=None):
    os.system('cls')
    print(f'{negritaText}\nAyuda de comandos:\n{negritaText}')
    [print(f'{negritaText}{item[0]} - {negritaText}{item[1]}') for item in commands]
    input('\nPresione cualquier botón para volver a la visualización del directorio actual . . . ')


def exit(userCommand, optionalParameter=None):
    continueMainLoop = False


def path(userCommand):
    if len(userCommand) > 2 and len(userCommand) < 1:
        input(f'{errorText}El comando "path" pide un solo parámetro para indicar la dirección de destino . . . {resetText}')
        return None
    try:
        os.chdir(userCommand[1])
    except:
        input(f'{errorText}Indicador de dirección especificada en parámetro no válido o no encontrado en contexto de directorio actual . . . {resetText}')


def back(userCommand, optionalParameter=None):
    if len(userCommand) > 1:
        input(f'{errorText}El comando "back" no requiere ni pide parámetros . . . {resetText}')
        return None
    
    try:
        os.chdir('..')
    except:
        input(f'{errorText}No se pudo cambiar al directorio raíz por un error interno o porque ese no se encontró . . . {resetText}')


def rename(userCommand):
    if len(userCommand) < 3 or len(userCommand) > 3:
        input(f'{errorText}El comando "rename" requiere para ser ejecutado un indicador de item requerido para el cambio de nombre y un nombre nuevo de este item . . . {resetText}')
        return None
    
    try:
        oldPath = indexAccess(userCommand[1], main.contextoAcual, True)
    except:
        oldPath = f'{os.getcwd()}\{os.listdir(os.getcwd())[int(userCommand[1])]}'        
    newPath = f'{os.getcwd()}\{userCommand[2]}'
    try:
        os.rename(oldPath, newPath)
    except:
        input(f'{errorText}No ha sido posible llevar a cabo el comando porque alguno de los parámetros ingresados no es válido{resetText}')


def search(userCommand):
    if len(userCommand) < 2 or len(userCommand) > 2:
        input(f'{errorText}El comando "search" requiere un parámetro correspondiente al filtro de buúsqueda con el que tengan que coincidir los items para ser mostrados . . . {resetText}')
        return None
    
    matches = []
    def search_in_directory(parent, search_term):
        local_matches = []
        for root, dirs, files in os.walk(parent):
            for file in files:
                if search_term in file:
                    path = os.path.join(root, file)
                    local_matches.append(path)
            for dir in dirs:
                if search_term in dir:
                    path = os.path.join(root, dir)
                    local_matches.append(path)
        return local_matches

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for parent, _, _ in os.walk(os.getcwd()):
            future = executor.submit(search_in_directory, parent, userCommand[1])
            matches.extend(future.result())

    return matches


def create(userCommand):
    if len(userCommand) < 3 or len(userCommand) > 3:
        input(f'{errorText}El comando "create" requiere dos parámetros: uno para indicar el tipo de creación (file o dir) y otro para el nombre de esta . . . {resetText}')
        return ''
    else:
        if userCommand[1] == 'folder':
            try:
                os.mkdir(userCommand[2])
            except:
                input(f'{errorText}El directorio no pudo ser creado. Podrían no ser suficientes los permisos de arministrador requeridos para accionar de esta manera en este directorio . . . {resetText}')
        elif userCommand[1] == 'file':
            try:
                open(userCommand[2], 'x')
            except:
                input(f'{errorText}El archivo no pudo ser creado. Podrían no ser suficientes los permisos de arministrador requeridos para accionar de esta manera en este directorio . . . {resetText}')
        else:
            input(f'{errorText}El segundo parámetro correspondiente al tipo de creación ingresado no es válido. Debe ser "file" o "dir" . . . {resetText}')


def delete(userCommand):
    exception = None
    try:
        deletingPath = indexAccess(userCommand[1], main.contextoActual, True)
    except:
        deletingPath = userCommand[1]
    try:
        os.remove(deletingPath)
    except:
        input(f'{errorText}El item indicado no pudo ser eliminado debido a que no se encontró el elemento o los permisos necesarios para realizar esta acción no alcanzan . . . {resetText}')
    

def move(userCommand):
    try:
        itemToMove = indexAccess(userCommand[1], main.contextoActual, True)
    except:
        itemToMove = userCommand[1]
    try:
        targetDirectory = indexAccess(userCommand[2], main.contextoActual, True)
    except:
        targetDirectory = userCommand[2]
    try:
        shutil.move(itemToMove, targetDirectory)
    except:
        input(f'{errorText}Los directorios o indices especificados para la acción no son válidos . . . {resetText}')