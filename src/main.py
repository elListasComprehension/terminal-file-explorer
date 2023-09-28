import os, functionModule as func

def main():
    userInput = 'terminal file explorer'
    while userInput[0] != 'exit':
        os.system("cls")
        func.showDirectoryContent(os.listdir(os.getcwd()))
        rawUserInput = func.takeUserInput()
        if rawUserInput is not None: 
            userInput = rawUserInput
            if userInput[0] == 'search':
                ultimoDirectorio = os.getcwd()
                conicidenciasSearch = func.search(userInput)
                if conicidenciasSearch is not None:
                    filtroBusqueda = userInput[1]
                    while ('back' not in userInput) or (os.getcwd() is not ultimoDirectorio):
                        os.system("cls")
                        func.showDirectoryContent(conicidenciasSearch, f"\n\n('{func.inputText}back{func.resetText}' para salir del menú de resultados) Actualmente mostrando la dirección o las direcciones de archivos o directorios coincidentes con '{func.negritaText}{filtroBusqueda}{func.resetText}':\n\n")
                        if len(conicidenciasSearch) == 0:
                            print("No se encontraron archivos o directorios que contengan el filtro de búsqueda.")
                        userInput = func.takeUserInput(conicidenciasSearch)
                        if userInput is not None:
                            if userInput[0] is 'search' or userInput[0] is 'path' or userInput[0] is 'create':
                                input("comando no valido en el contexto actual")
                            elif userInput[0] is not 'back':
                                func.detectCommand(userInput, conicidenciasSearch)
            else:
                func.detectCommand(userInput)

if __name__ == '__main__':
    main()