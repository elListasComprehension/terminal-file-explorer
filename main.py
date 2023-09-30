import os, functionModule as func

def main():
    while func.continueLoop:
        os.system("cls")
        func.showDirectoryContent(os.listdir(os.getcwd()))
        isSearching, userInput = func.detectCommand(func.takeUserInput())
        if isSearching:
            while func.contineSearchMenuLoop:
                resultadosSearch = func.search(userInput)
                if resultadosSearch == []:
                    print(f"{func.negritaText} No se encontraron archivos o directorios que contengan el filtro de búsqueda.{func.resetText}")
                    input('\n\n Presione cualquier botón para continuar . . . ')
                else:
                    func.showDirectoryContent(resultadosSearch, f"\n\n('{func.inputText}exit{func.resetText}' para salir del menú de resultados) Actualmente mostrando la dirección o las direcciones de archivos o directorios coincidentes con '{func.negritaText}{userInput[1]}{func.resetText}':\n\n")
                    userInput = func.takeUserInput()
                    if userInput:
                        if userInput[0] == 'search' or userInput[0] == 'path' or userInput[0] == 'create' or userInput[0] == 'back':
                            input("comando no valido en el contexto actual")
                        if userInput[0] == 'exit':
                            func.exit(userInput, True)
                        else:
                            func.detectCommand(userInput)

if __name__ == '__main__':
    main()