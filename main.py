import os, functionModule as func

def main():
    while func.contineLoop:
        os.system("cls")
        func.showDirectoryContent(os.listdir(os.getcwd()))
        isSearching, userInput = func.detectCommand(func.takeUserInput())
        if isSearching:
            while func.search.contineSearchMenuLoop:
                resultadosSearch = func.search(userInput)
                if resultadosSearch is None:
                    if resultadosSearch == []:
                        print(f"{func.negritaText} No se encontraron archivos o directorios que contengan el filtro de búsqueda.{func.resetText}")
                    else:
                        func.showDirectoryContent(resultadosSearch, f"\n\n('{func.inputText}back{func.resetText}' para salir del menú de resultados) Actualmente mostrando la dirección o las direcciones de archivos o directorios coincidentes con '{func.negritaText}{userInput[1]}{func.resetText}':\n\n")

'''
if userInput[0] == 'search':
                ultimoDirectorio = os.getcwd()
                conicidenciasSearch = func.search(userInput)
                filtroBusqueda = userInput[1]
                while ('back' not in userInput) or (ultimoDirectorio is os.getcwd()):
                    os.system("cls")
                    func.showDirectoryContent(conicidenciasSearch, f"\n\n('{func.inputText}back{func.resetText}' para salir del menú de resultados) Actualmente mostrando la dirección o las direcciones de archivos o directorios coincidentes con '{func.negritaText}{filtroBusqueda}{func.resetText}':\n\n")
                    if len(conicidenciasSearch) == 0:
                        print(f"{func.negritaText} No se encontraron archivos o directorios que contengan el filtro de búsqueda.{func.resetText}")
                    userInput = func.takeUserInput(conicidenciasSearch)
                    if userInput is not "":
                        if userInput[0] is 'search' or userInput[0] is 'create':
                            input("comando no valido en el contexto actual")
                        elif userInput[0] is not 'back':
                            func.detectCommand(userInput, conicidenciasSearch)
                        else:
                            pass
'''


if __name__ == '__main__':
    main()