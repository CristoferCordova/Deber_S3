from POO_semana3 import Ciudad
first_ciry = Ciudad("Quito")

def main():
    first_ciry.ingreso_temperaturas()
    print()
    print(f"el promedio semanal de la ciudad de {first_ciry.ciudad} es de {first_ciry.calculo_promedio()}")

if __name__ == "__main__":
    main()