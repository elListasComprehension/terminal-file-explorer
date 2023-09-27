# 💾 explorador de archivos estilo terminal

explorador de archvivos hecho en python para un proyecto de secundaria

manual de usuario: https://docs.google.com/document/d/1JlERBnCr5ed9yySsSNRMDKvBj9T4Lj6PfHrGharcXS0/edit?usp=sharing


## Guía para desarrolladores


el siguiente es el primer vistazo que uno tendrá del programa donde, tal como si fuese el explorador de archivos de Windows, este mostrará los diferentes elementos que existan dentro del directorio actual (current working directory o cwd).

![image](https://github.com/elListasComprehension/terminal-file-explorer/assets/142759837/d224e6df-85a9-43d3-8c26-383a018acf67)


el algoritmo consiste de un bucle de programa (que dura hasta que se ingrese la palabra reservada 'exit') que contiene la simple lógica que exige el ingreso del input del usuario y que existe dentro de un archivo main.py, el cual, además, importa las diferentes funciones del módulo functionModule.py como se ve en las siguientes imágenes.

![image](https://github.com/elListasComprehension/terminal-file-explorer/assets/142759837/cce99942-bfcc-45ab-8fa0-952029b1e76a)

<br>

archivo 'main.py':

![image](https://github.com/elListasComprehension/terminal-file-explorer/assets/142759837/84c78be4-eaae-4153-a474-1781c1ea24df)


### Bucle de programa

En cada iteración del programa se llamará a diferentes funciones y dos de ellas son: showDirectoryContent (para mostrar el contenido del cwd como lo exigiría un softeare como un         explorador de archivos) y takeUserInput. Ésta última se encargará de ejecutar la función 'input()' y analizar el valor guardado para realizar un primer filtrado que determine si el      primer token del string ingresado es una de las palabras o comandos reservados del programa. En el caso en el que no exista una coincidencia entre el comando ingresado y los comandos de la lista de los válidos la función takeUserInput devolverá 'None' (por eso se chequea que el valor en rawUserInput sea diferente de None antes de hacerle el parsing); en cambio, si la función encuentra una concidencia entre el primer token del usuario y los comandos válidos devolverá el input del usuario, que se seguirá tokenizando y parseando dentro de los siguientes pasos que explicaremos luego. Antes explicaremos la dinámica de la sintaxis de los comandos:

![image](https://github.com/elListasComprehension/terminal-file-explorer/assets/142759837/93b8d140-9da7-4d70-a780-9fc1a4ea1a3a)


#### Sintaxis de comandos

Este es un ejemplo de comando que podría ingresar el usuario. Todos los comandos que ingrese el usuario (a excepción de un tipo) incluirán: la palabra reservada, en el caso de arriba 'path'; y los parámetros que esa función pueda pedir, en este mismo caso, un indicador válido de dirección de directorio (como 'C:/ProgramFiles' o '..'); además, la palabra reservada y los parámetros deberán estar separados por espacios, para facilitar el sistema de tokenization (el desuso de los espacios podría llevar a malas interpretaciones del input y al acarreamiento de errores relacionados con parámetros inválidos). Los parámetros pedidos variarán entre funciones pero la mayoría pedirán entre uno y tres de estos.


