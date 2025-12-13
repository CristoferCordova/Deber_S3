class Ciudad:
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.temperaturas = []
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Vienres", "Sábado", "Domingo"]
    

    
    def ingreso_temperaturas(self):
        for dia in self.dias:
            temperatura = float(input(f"Ingrese el valor de la temperatura para {dia}: "))
            self.temperaturas.append(temperatura)
    

    def calculo_promedio(self):
        suma = 0
        n = 0
        for temperatura in self.temperaturas:
            suma+= temperatura
            n += 1
        promedio = suma /n
        return round(promedio, 2)
    
    

    



