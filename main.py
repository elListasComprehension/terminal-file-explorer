import os, functionModule as func
isSearching = False
def main():
    while func.continueLoop:
        os.system('cls')
        contextoActual = os.listdir(os.getcwd())
        func.showDirectoryContent(contextoActual)
        isSearching, userInput = func.detectCommand(func.takeUserInput())
        if isSearching:
            func.continueSearchMenuLoop = True
            while func.continueSearchMenuLoop:
                os.system('cls')
                resultadosSearch = func.search(userInput)
                if resultadosSearch == []:
                    input(f'{func.negritaText} No se encontraron archivos o directorios que contengan el filtro de búsqueda.{func.resetText}\n\n Presione cualquier botón para continuar . . . ')
                    func.continueSearchMenuLoop = False
                else:
                    contextoActual = resultadosSearch
                    func.showDirectoryContent(contextoActual, f"\n\n('{func.inputText}exit{func.resetText}' para salir del menú de resultados) Actualmente mostrando la dirección o las direcciones de archivos o directorios coincidentes ':\n\n")
                    func.detectCommand(func.takeUserInput(resultadosSearch))

if __name__ == '__main__':
    main()