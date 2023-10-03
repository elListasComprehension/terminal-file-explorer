import os, functionModule as func

def main():
    while func.continueLoop:
        os.system('cls')
        func.showDirectoryContent(os.listdir(os.getcwd()))
        isSearching, userInput = func.detectCommand(func.takeUserInput())
        if isSearching:
            while func.continueSearchMenuLoop:
                os.system('cls')
                resultadosSearch = func.search(userInput)
                if resultadosSearch == []:
                    input(f'{func.negritaText} No se encontraron archivos o directorios que contengan el filtro de búsqueda.{func.resetText}\n\n Presione cualquier botón para continuar . . . ')
                    func.continueSearchMenuLoop = False
                else:
                    func.showDirectoryContent(resultadosSearch, f"\n\n('{func.inputText}exit{func.resetText}' para salir del menú de resultados) Actualmente mostrando la dirección o las direcciones de archivos o directorios coincidentes ':\n\n")
                    func.detectCommand(func.takeUserInput(resultadosSearch))

if __name__ == '__main__':
    main()