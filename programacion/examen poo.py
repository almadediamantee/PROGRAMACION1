class rectangulo:
    def _init_(self, Longitud, Ancho ):
        self.Longitud= Longitud
        self.Ancho= Ancho 


    def _calcular_area(self, Longitud,Ancho ):
        self.Longitud * self.Ancho

    def _calcular_perimetro( self, Longitud, Ancho):
        (self.Longitud + self.Ancho) * 2


obj1=rectangulo(4,4) 
print(f"el area del rectangulo es : {obj1.calcular_area}")

print(f"el perimetro del rectangulo es :{obj1.calcular_perimetro}" )





        
