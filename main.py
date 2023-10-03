import os, functionModule as func

def main():
    while func.continueLoop:
        os.system("cls")
        func.showDirectoryContent(os.listdir(os.getcwd()))
        isSearching, userInput = func.detectCommand(func.takeUserInput())
        if isSearching:
            while func.continueSearchMenuLoop:
                resultadosSearch = func.search(userInput)
                if resultadosSearch == []:
                    print(f"{func.negritaText} No se encontraron archivos o directorios que contengan el filtro de búsqueda.{func.resetText}")
                    input('\n\n Presione cualquier botón para continuar . . . ')
                    func.continueSearchMenuLoop = False
                else:
                    func.showDirectoryContent(resultadosSearch, f"\n\n('{func.inputText}exit{func.resetText}' para salir del menú de resultados) Actualmente mostrando la dirección o las direcciones de archivos o directorios coincidentes ':\n\n")
                    userInput = func.takeUserInput()
                    if userInput:
                        if userInput[0] == 'search' or userInput[0] == 'path' or userInput[0] == 'create' or userInput[0] == 'back' or userInput[0] == 'exit':
                            if userInput[0] == 'exit':
                                func.exit(userInput, True)
                            else:
                                input("comando no valido en el contexto actual")
                        else:
                            func.detectCommand(userInput, resultadosSearch)

if __name__ == '__main__':
    main()