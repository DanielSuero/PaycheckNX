print(" /$$$$$$$                               /$$                           /$$             /$$   /$$ /$$   /$$")
print("| $$__  $$                             | $$                          | $$            | $$$ | $$| $$  / $$")
print("| $$  \ $$ /$$$$$$  /$$   /$$  /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$      | $$$$| $$|  $$/ $$/")
print("| $$$$$$$/|____  $$| $$  | $$ /$$_____/| $$__  $$ /$$__  $$ /$$_____/| $$  /$$/      | $$ $$ $$ \  $$$$/ ")
print("| $$____/  /$$$$$$$| $$  | $$| $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/       | $$  $$$$  >$$  $$ ")
print("| $$      /$$__  $$| $$  | $$| $$      | $$  | $$| $$_____/| $$      | $$_  $$       | $$\  $$$ /$$/\  $$")
print("| $$     |  $$$$$$$|  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$      | $$ \  $$| $$  \ $$")
print("|__/      \_______/ \____  $$ \_______/|__/  |__/ \_______/ \_______/|__/  \__/      |__/  \__/|__/  |__/")
print("                    /$$  | $$                                                                            ")
print("                   |  $$$$$$/                                                                            ")
print("                    \______/                                                                             ")

nombre = input ("Bienbenido, por favor, identifiquese solo con su nombre ")

valor = int(input("Bienvenido, "+ nombre +", Por favor, introduzca el valor de una hora de trabajo "))

hora = int(input("Por favor, introduzca la cantidad de horas trabajadas en una semana "))


semana = valor * hora

mes = semana * 4

anual = mes * 14


print ("Su valor semanal es de " + str(semana) + " Euros")

print ("Su valor mensual es de " + str(mes) + " Euros")

print ("Su valor anual es de " + str(anual) + " Euros")

input("Pulse cualquier tecla para cerrar el programa")