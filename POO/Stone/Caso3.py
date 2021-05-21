class triangulo:
    def __init__(self,base,lado_i,lado_d):
        self.base = base
        self.lado_i = lado_i
        self.lado_d = lado_d
    
    def mayoLado(self):
        print(max(self.base,self.lado_i,self.lado_d))

    def tipo(self):
        if self.base == self.lado_i  and self.base == self.lado_d :
            print("Triangulo equilatero")
        elif self.base != self.lado_i  and self.base != self.lado_d and self.lado_d == self.lado_d:
            print("Trianulo isoseles")
        else:
            print("Trianglo escaleno")

def main():
    base = int(input("Ingrese la base del triangulo: "))
    l1 = int(input("Ingrese uno de los lados: "))
    l2 = int(input("Ingrese otro de los lados: "))
    tri = triangulo(base,l1,l2) 
    tri.mayoLado()
    tri.tipo()

main()