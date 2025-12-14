class Ciudad:
    def __init__(self, ciudad): #clase con sus atributos, ciudad, temepraturas y días de la semana
        self.ciudad = ciudad
        self.temperaturas = [] # se crea una lista vacía, el usuario va a ir ingresando las temepraturas
        self.dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Vienres", "Sábado", "Domingo"]
    

    
    def ingreso_temperaturas(self): # se crea una método para el ingreso de las temepraturas en la lista vacía 
        for dia in self.dias:
            temperatura = float(input(f"Ingrese el valor de la temperatura para {dia}: "))
            self.temperaturas.append(temperatura)
    

    def calculo_promedio(self):     #Se crea un método que me cálcula el promedio de las temperatura por días
        suma = 0
        n = 0
        for temperatura in self.temperaturas:
            suma+= temperatura
            n += 1
        promedio = suma /n
        return round(promedio, 2)
    
    

    



