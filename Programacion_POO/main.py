from POO_semana3 import Ciudad # se importa la clase 
first_ciry = Ciudad("Quito") # se crea el primer objeto 

def main():
    first_ciry.ingreso_temperaturas() #se utiliza el método de ingresar temepraturas
    print()
    print(f"el promedio semanal de la ciudad de {first_ciry.ciudad} es de {first_ciry.calculo_promedio()}") #se imprime el mensaje final

if __name__ == "__main__":
    main()