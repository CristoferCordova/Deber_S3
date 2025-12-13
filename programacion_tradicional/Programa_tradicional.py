#definicion de variables 
temperaturas = []
ciudad = input("Ingresa el nombre de la ciuda: ")
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Vienres", "Sábado", "Domingo"]


# definción de funciones

def agregar_temepraturas(lista, dias):
    for dia in dias:
        temperatura = float(input(f"Ingrese la temperatura del {dia} es: "))
        lista.append(temperatura)

def calculo_temperatura(lista_temepraturas):
    suma = 0
    n=0
    for temperatura in lista_temepraturas:
       
        suma += temperatura
        n+=1
    return round(suma/n, 2)
    
# ejecución de las funciones
def main ():
    agregar_temepraturas(temperaturas, dias_semana)

    print(f"la temepratura promedio en el fin de semana en la ciduad {ciudad} es {calculo_temperatura(temperaturas)}")

if __name__ == "__main__":
    main()
