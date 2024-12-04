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

# En las siguientes 4 lineas de codigo se recogen los datos del usuario
    
    nombre = input ("Bienbenido, por favor, identifiquese solo con su nombre ")

    valor = int(input("Bienvenido, "+ nombre +", Por favor, introduzca el valor de una semana de trabajo "))

    hora = int(input("Por favor, introduzca la cantidad de horas trabajadas en una semana "))

    tarea = input("¿De que desea saber el valor?")

# En las siguientes lineas de codigo se calculan los diferentes valores en función de la tarea que le pide al usuario al programa
    
    if tarea == "Hora" or tarea == "hora" or tarea == "Una hora" or tarea == "una hora":

        valorhora = valor / hora
        print ("Su valor por hora es de " + str(valorhora) + " Euros")


    elif tarea == "Mes" or tarea == "mes" or tarea == "Mensual" or tarea == "mensual":
    
        valormes = valor * 4
        print ("Su valor mensual es de " + str(valormes) + " Euros")


    elif tarea == "Año" or tarea == "año" or tarea == "Anual" or tarea == "anual":

        valoranual = valor * 48
        print ("Su valor anual es de " + str(valoranual) + " Euros")

    else: 
        
        print("No he entendido a que se refiere, por favor vuelva a introducir sus datos")


    fin = input("¿Desea finalizar el programa?")
