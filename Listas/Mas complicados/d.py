pila_1 = []
pila_2 = []
pila_3 = []
pila_4 = []
pila_5 = []

def ingresar(elemento):
   if len(pila_1) < 5:
      pila_1.append(elemento)
      return"pila_1"
   elif len(pila_2) < 5:
      pila_2.append(elemento)
      return"pila_2"
   elif len(pila_3) < 5:
      pila_3.append(elemento)
      return "pila_3"
   elif len(pila_4) < 5:
      pila_4.append(elemento)
      return "pila_4"
   elif len(pila_5) < 5:
      pila_5.append(elemento)
      return "pila_5"
   else:
      return None #Retorna none si no existe mas lugar
   
def retirar(a):
   if a.lower() == 'pila_1' and len(pila_1) > 0:
      return pila_1.pop()
   elif a.lower() == 'pila_2' and len(pila_2) > 0:
      return pila_2.pop()
   elif a.lower() == 'pila_3' and len(pila_3) > 0:
      return pila_3.pop()
   elif a.lower() == 'pila_4' and len(pila_4) > 0:
      return pila_4.pop()
   elif a.lower() == 'pila_5' and len(pila_5) > 0:
      return pila_5.pop()
   else:
      return None #Retorna none si no existe la pila o ya no hay elementos en dicha pila

while True:
   opcion = input('\n¿Qué desea hacer?\n1) Ingesar\n2) Retirar\n3) Salir\n>>')
   if opcion == "1":
      elemento = input('Cargar: ')
      resultado = ingresar(elemento)
      presentacion=['Operacion Fallida','Operacion exitosa, se cargo {} en {}'.format(elemento,resultado)][resultado != None]
      print(presentacion)
   elif opcion == "2":
      pila = input('De que pila desea retirar.? (pila_1, pila_2, pila_3, pila_4, pila_5): ')
      resultado = retirar(pila)
      presentacion=['Operacion Fallida','Operacion exitosa, se retiro {}'.format(resultado)][resultado != None]
      print(presentacion)
   elif opcion == "3":
      break
   else:
      print('Entrada no valida')

