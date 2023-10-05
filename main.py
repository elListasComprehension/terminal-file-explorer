import os, functionModule as func

def main():
    searching = None
    while func.continueMainLoop:
        os.system('cls')
        
        if not searching:
            upperMesseage = f'{func.negritaText}Current directory is: {os.getcwd()}\n{func.resetText}'
            contextoActual = [os.path.join(os.getcwd(), item) for item in os.listdir(os.getcwd())]
            func.showDirectoryContent(contextoActual, upperMesseage, True)
        else:
            func.showDirectoryContent(contextoActual, upperMesseage, False)

        searching = func.detectCommand(func.takeUserInput(contextoActual), searching, contextoActual)
        
        if searching:
            upperMesseage = f'\n\n("{func.inputText}exit{func.resetText}" para salir del menú de resultados) Actualmente mostrando la dirección o las direcciones de archivos o directorios coincidentes:\n\n'
            contextoActual = func.search(searching)
            if contextoActual == []:
                searching = None
                input(f'{func.negritaText} No se encontraron archivos o directorios que contengan el filtro de búsqueda.{func.resetText}\n\n Presione cualquier botón para continuar . . . ')

if __name__ == '__main__':
    main()