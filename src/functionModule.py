import os, shutil

errorText, negritaText, inputText, resetText, colorCeleste = "\033[91;4m", "\033[1m", "\033[1;33m", "\033[0m", "\033[1;36m"

commands = [
    ['help', f'Mostrar la descripción de comandos disponibles junto a un ejemplo de uso. ________ {inputText}"help"{resetText}'],
    ['path', f'Cambiar el directorio al especificado indicado por parámetro. ____________________ {inputText}"path C:/Windows"{resetText}'],
    ['back', f'Retroceder al directorio raís del directorio actual o current working directory. _ {inputText}"back"{resetText}'],
    ['copy', f'Copiar el directorio o archivo indicado a una dirección especificada. ____________ {inputText}"copy"{resetText}'],
    ['move', f'Mover un archivo o directorio ingresado a otra dirección. ________________________ {inputText}"move .../archivo .../carpeta"{resetText}'],
    ['rename', f'Cambiar el nombre de un archivo o directorio. __________________________________ {inputText}"rename C:/ProgramFiles/Firefox Chrome"{resetText}'],
    ['create', f'Crear un nuevo archivo o directorio indicando tipo y nombre. ___________________ {inputText}"create file imagen.jpg"{resetText}'],
    ['search', f'Buscar archivos o directorios por nombre en el directorio actual. ______________ {inputText}"search carpeta"{resetText}'],
    ['delete', f'Borrar un archivo o directorio indicado. _______________________________________ {inputText}"delete C:/Users/Public/Desktop/carpeta"{resetText}'],
    ['exit', f'Salir del programa. {inputText}"exit"{resetText}']
]

def showDirectoryContent(directory, optionalParameter=None): #muestra en un formato de lista con índices el contenido de archivos y carpetas 
    if optionalParameter is None:
        print(f"{negritaText}Current directory is: {directory}\n{resetText}")
    else:
        print(optionalParameter)
    try:
        for i, item in enumerate(os.listdir(directory)):
            if os.path.isdir(os.path.join(directory, item)):
                print(f'    {i} - {colorCeleste}[D]{resetText} {item}')
            else:
                print(f'    {i} - {inputText}[F]{resetText} {item}')
    except:
        input("Acceso denegado a carpeta. Pruebe aumentando los permisos con los que el programa corre . . . ")

def takeUserInput(indexedItemsList=None): # toma el input del usuario y le hace un filtrado inicial
    if indexedItemsList is None:
        indexedItemsList = os.listdir(os.getcwd())
    returnInput = str(input(f"{inputText}\n >>> {resetText}"))
    returnInput = returnInput.split(" ")
    if returnInput[0] not in [item[0] for item in commands]:
        try:
            int(returnInput)
        except:
            input(f"{errorText}{returnInput[0]} no se reconoce como un comando interno o externo, programa o archivo por lotes ejecutable . . . {resetText}")
            return None
        if int(returnInput) < 0 or int(returnInput) > (len(indexedItemsList)) - 1:
            input(f"{errorText}Número de índice ingresado fuera de rango en el contexto de directorio actual . . . {resetText}")
            return None
        else:
            return returnInput
    else:
        return returnInput

def detectCommand(userCommand, optionalParameter=None): #Enviar a función a partir de comandos
    try:
        int(userCommand)
    except:
        if userCommand[0] == 'exit':
            pass
        else:
            exec(f"{userCommand[0]}({userCommand}, {optionalParameter})")
        return ""
    fileIndexAccess(userCommand)

def fileIndexAccess(userCommand, indexedItemsList=None, functionCalled=None): #usar número de índice para acceder
    if indexedItemsList is None:
        indexedItemsList = os.listdir(os.getcwd())
    if functionCalled is not None:
        if int(userCommand) < 0 or int(userCommand) > (len(indexedItemsList)) - 1:
            input("")
            return ""
        else:
            return indexedItemsList[int(userCommand)]
    else:
        if '.' in indexedItemsList[int(userCommand)]:
            try:
                if indexedItemsList == os.listdir(os.getcwd()):
                    os.startfile(f'{os.path.join(os.getcwd(), indexedItemsList[int(userCommand)])}')
                else:
                    os.startfile(f'{indexedItemsList[int(userCommand)]}')
            except:
                input(f"{errorText}No se logró ejecutar el programa seleccionado . . . {resetText}")
        else:
            try:
                os.chdir(indexedItemsList[int(userCommand)])
            except:
                input(f"{errorText}Acceso denegado a directorio. Pruebe aumentando los permisos con los que el programa corre . . . {resetText}")

def help(userCommand, optionalParameter=None): #mostrar una descripción de los comandos que inluye el programa
    os.system("cls")
    print(f"{negritaText}\nAyuda de comandos:\n{negritaText}")
    [print(f"{negritaText}{item[0]} - {negritaText}{item[1]}") for item in commands]
    input("\nPresione cualquier botón para volver a la visualización del directorio actual . . . ")

def path(userCommand, optionalParameter=None): #Cambiar el directorio
    if len(userCommand) > 2 and len(userCommand) < 1:
        input("")
    else:
        try:
            os.chdir(userCommand[1])
        except:
            input(f"{errorText}Indicador de dirección especificada en parámetro no válido o no encontrado en contexto de directorio actual . . . {resetText}")

def back(userCommand, optionalParameter=None): #ir al directorio previo
    if len(userCommand) > 1:
        input(f"{errorText}El comando 'back' no requiere ni pide parámetros . . . {resetText}")
    else:
        try:
            os.chdir("..")
        except:
            input(f"{errorText}No se pudo cambiar al directorio raíz por un error interno o porque ese no se encontró . . . {resetText}")

def rename(userCommand, optionalParameter=None): # renombrar archivos en directorio actual
    if len(userCommand) < 3 or len(userCommand) > 3:
        input(f"{errorText}El comando 'rename' requiere para ser ejecutado un indicador de item requerido para el cambio de nombre y un nombre nuevo de este item . . . {resetText}")
        return ""
    exception = None
    try:
        int(userCommand[1])
    except:
        exception = True
        oldPath = f'{os.getcwd()}\{os.listdir(os.getcwd())[int(userCommand[1])]}'
    if exception is None:
        oldPath = fileIndexAccess(userCommand[1], None, True)
    newPath = f'{os.getcwd()}\{userCommand[2]}'
    try:
        os.rename(oldPath, newPath)
    except:
        input(f"{errorText}No ha sido posible llevar a cabo el comando porque alguno de los parámetros ingresados no es válido")

def search(userCommand, optionalParameter=None):
    if len(userCommand) < 2 or len(userCommand) > 2:
        input("el comando search requiere un parametro para el filtro de busqueda")
        return ""
    
    matches = []
    itemsRecorridos = 0
    userInput = ""

    for parent, directorios, archivos in os.walk(os.getcwd()):
        itemsRecorridos += 1
        os.system("cls")
        print(f"Buscando en {itemsRecorridos} items . . . ")
        for archivo in archivos:
            if userCommand[1] in archivo:
                pathCompleto = os.path.join(parent, archivo)
                matches.append(pathCompleto)
        for directorio in directorios:
            if userCommand[1] in directorio:
                pathCompleto = os.path.join(parent, directorio)
                matches.append(pathCompleto)

    while userInput != 'back':
        os.system("cls")
        print(f"\n\n('{inputText}back{resetText}' para salir del menú de resultados) Actualmente mostrando la dirección o las direcciones de archivos o directorios coincidentes con '{negritaText}{userCommand.split(' ')[1]}{resetText}':\n\n")
        [print(f"{i} - {path}") for i, path in enumerate(matches)]
        rawUserInput = takeUserInput(matches)
        if rawUserInput is not None:
            userInput = rawUserInput
            try: 
                int(userInput)
            except:
                if userInput is 'back':
                    return ""
                else:
                    input("comando no valido en el contexto actual de navegacion de datos")
            finally:
                if (int(userInput) >= 0 and int(userInput) < len(matches)):
                    fileIndexAccess(userCommand, matches)
                    return ""
                else:
                    input("index fuera de rango de lista de resultados")

def create(userCommand, optionalParameter=None):
    input(f'{userCommand} {len(userCommand)}')
    if len(userCommand) < 3 or len(userCommand) > 3:
        input("el comando create requiere dos parámetros: uno para especificar el tipo de creación y otro para el nombre de esta.")
        return ""
    else:
        if userCommand[1] == 'folder':
            try:
                os.mkdir(userCommand[2])
            except:
                input("El directorio no pudo ser creado.")
        elif userCommand[1] == 'file':
            try:
                open(userCommand[2], "x")
            except:
                input("El archivo no pudo ser creado")
        else:
            input("No es un parametro valido.")

def delete(userCommand, optionalParameter=None):
    exception = None
    try:
        int(userCommand[1])
    except:
        exception = True
        deletingPath = userCommand[1]
    if exception is None:
        deletingPath = fileIndexAccess(userCommand[1], None, True)
    os.remove(deletingPath)
    

def move(userCommand, optionalParameter=None):
    input(f'{os.path.join(os.getcwd(), os.listdir(os.getcwd())[userCommand[1]])}, {userCommand[2]}')
    try:
        int(userCommand[1])
    except:
        try:
            shutil.move(userCommand[1], userCommand[2])
            return ""
        except:
            input("los parámetros de direcciones no son válidos")
            return ""
    try:
        shutil.move(os.path.join(os.getcwd(), os.listdir(os.getcwd())[userCommand[1]]), userCommand[2])
        return ""
    except:
        input("numero de indice invalido en el contexto actual o segundo parametro de direccion invalido.")
        return ""

def copy(userCommand, optionalParameter=None):
    pass