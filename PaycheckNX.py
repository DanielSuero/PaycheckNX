print(r" /$$$$$$$                               /$$                           /$$             /$$   /$$ /$$   /$$")
print(r"| $$__  $$                             | $$                          | $$            | $$$ | $$| $$  / $$")
print(r"| $$  \ $$ /$$$$$$  /$$   /$$  /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$      | $$$$| $$|  $$/ $$/")
print(r"| $$$$$$$/|____  $$| $$  | $$ /$$_____/| $$__  $$ /$$__  $$ /$$_____/| $$  /$$/      | $$ $$ $$ \  $$$$/ ")
print(r"| $$____/  /$$$$$$$| $$  | $$| $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/       | $$  $$$$  >$$  $$ ")
print(r"| $$      /$$__  $$| $$  | $$| $$      | $$  | $$| $$_____/| $$      | $$_  $$       | $$\  $$$ /$$/\  $$")
print(r"| $$     |  $$$$$$$|  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$      | $$ \  $$| $$  \ $$")
print(r"|__/      \_______/ \____  $$ \_______/|__/  |__/ \_______/ \_______/|__/  \__/      |__/  \__/|__/  |__/")
print(r"                    /$$  | $$                                                                            ")
print(r"                   |  $$$$$$/                                                                            ")
print(r"                    \______/                                                                          1.0")


fin = ""
while fin != "si":


    nombre = input ("Bienbenido, por favor, identifiquese solo con su nombre ")

    valor = int(input("Bienvenido, "+ nombre +", Por favor, introduzca el valor de una hora de trabajo "))

    hora = int(input("Por favor, introduzca la cantidad de horas trabajadas en una semana "))

    tarea = input("¿De que desea saber el valor?")


    if tarea == "semana" or tarea == "Semana" or tarea == "semanal" or tarea == "Semanal":

        semana = valor * hora
        print ("Su valor semanal es de " + str(semana) + " Euros")


    elif tarea == "Mes" or tarea == "mes" or tarea == "Mensual" or tarea == "mensual":
    
        mes = hora * 4
        valormes = valor * mes
        print ("Su valor mensual es de " + str(valormes) + " Euros")


    elif tarea == "Año" or tarea == "año" or tarea == "Anual" or tarea == "anual":

        anual = hora * 48
        valoranual = valor * anual
        print ("Su valor anual es de " + str(valoranual) + " Euros")

    else: 
        
        print("No he entendido a que se refiere, por favor vuelva a introducir sus datos")


    fin = input("¿Desea finalizar el programa?")
