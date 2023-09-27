import os, functionModule as func

def main():
    userInput = 'terminal file explorer'
    while userInput[0] != 'exit':
        os.system("cls")
        func.showDirectoryContent(os.getcwd())
        rawUserInput = func.takeUserInput()
        if rawUserInput is not None: 
            userInput = rawUserInput
            func.detectCommand(userInput)

if __name__ == '__main__':
    main()