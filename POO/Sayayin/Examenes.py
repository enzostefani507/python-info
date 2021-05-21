#Vamos a contribuir con la educación virtual, programando test online.
#El enunciado de un examen consta de preguntas. 
#Una pregunta se caracteriza por las siguientes propiedades (que se pueden consultar en cualquier momento): 

#- 	Texto: corresponde con una cadena que contiene el enunciado completo de la pregunta. 
#- 	Respuesta correcta: es una cadena que representa la respuesta correcta. 
#- 	Dificultad: número entero mayor o igual que cero que indica la dificultad de la pregunta. 

#Las preguntas se crean estableciendo el texto de la pregunta y la respuesta correcta. 
#Inicialmente todas las preguntas tienen un valor 0 de dificultad. 

#Por su parte, las propiedades que caracterizan a un enunciado de examen son: 
#- 	Nombre: una cadena que identifica el examen. 
#- 	Preguntas: lista que almacena la secuencia de preguntas del examen. 
			   #El orden de las preguntas en la secuencia es importante. 
#- 	Número de preguntas. Al construir un enunciado de examen sólo se establece el nombre, 
						#las preguntas se van añadiendo a posteriori. 

#La gestión de las preguntas incluye: 
#- 	Añadir pregunta: inserta la pregunta al final del examen.
#- 	Obtener pregunta: dado el número de una pregunta, retorna la pregunta. 
					  #Nótese que la primera pregunta (n 1) del examen corresponde con el índice 0 de la colección.
					  #El método devolverá null en el caso de que no exista una pregunta para el número solicitado.
#- 	Permutar pregunta: dado el núm de una pregunta, se mueve la pregunta a la posición representada por otro núm.
					   #Por ejemplo, mover la pregunta 3 a la posición 1. El método devuelve un valor booleano 
					   #para indicar si la operación se ha realizado con éxito o no. 
					   #No tendrá éxito si los números de las preguntas no son válidos. 
#- 	Borrar pregunta: la clase ofrece dos versiones diferentes para el borrado de preguntas. 
					 #En una de ellas se recibe como parámetro un número de pregunta y en la otra una pregunta. 
					 #En cualquiera de los dos casos, el resultado es que la pregunta se borra del examen. 
					 #El método devuelve un valor booleano p indicar si la operación se realizó con éxito o no.
#- 	Contiene pregunta: Devuelve un valor booleano que indica si la pregunta forma parte, o no, 
					   #del enunciado del examen 

#Un examen representa las respuestas a las preguntas de un enunciado de examen. Se caracteriza por: 
#- 	Un identificador: número entero q identifica a la resolución. Este identificador será calculado automáticamente
					  #para cada resolución y se asignarán identificadores secuenciales a partir de 1. 
					  #Esta propiedad no varía.
#- 	Enunciado de examen: el enunciado de examen al que corresponden las respuestas. Esta propiedad no varía. 
#- 	Respuestas: colección (mapa) que asocia preguntas con respuestas. 

#La funcionalidad de un examen es la siguiente: 
#- 	Responder: establece la respuesta para una pregunta del examen. 
			   #Este método recibe como parámetro el número de la pregunta y la respuesta a esta pregunta. 
			   #En la ejecución del método se comprueba que el número de pregunta sea válido y, en su caso, 
			   #se registra la asociación de la pregunta, correspondiente al número establecido, y la respuesta. 
			   #Finalmente, devuelve un valor booleano que indica si la operación se ha realizado con éxito o no. 
			   #Se puede responder más de una vez a la misma pregunta, cada respuesta sustituirá a la anterior. 

class Pregunta:
	def __init__(self, texto='', rta='', dif=0):
		self.texto = texto
		self.rta = rta
		self.dif = dif

	def start(self):
		self.set_texto()
		self.set_rta()
		self.set_dif()
#Pregunta.start()
	def set_texto(self):
		self.texto = input("Ingrese el texto de la pregunta:\n")

	def set_rta(self):
		self.rta = input("Ingrese la respuesta correcta:\n")

	def set_dif(self):
		self.dif = int(input("Ingrese la dificultad de la pregunta del 1 al 10: "))

	def __str__(self):
		return f'¿{self.texto}?'



registro_respuestas = []
class Respuestas:
	def __init__(self, examen):
		self.examen = examen
		self.nombre = ''
		self.respuestas = []
		self.ident = len(registro_respuestas)+1
		self.agregar_a_registro()

	def agregar_a_registro(self):
		registro_respuestas.append(self)

	def start(self):
		i = 1
		self.nombre = input("Ingrese su nombre: ")
		for pregunta in self.examen.preguntas:
			print(f'Pregunta n° {i}: {pregunta}')
			rta = input("Ingrese su respuesta:\n>>")
			
			if pregunta.rta == rta:
				self.respuestas.append((rta, 1))
			else:
				self.respuestas.append((rta, 0))
			i += 1

	def obtener_puntaje(self):
		puntaje = 0
		for respuesta in self.respuestas:
			if respuesta[1] == 1:
				puntaje += 1
		print(f'El puntaje total es: {puntaje}')

	def mostrar_examen(self):
		i = 0
		print(f'NOMBRE DEL EXAMEN: {self.examen.nombre}')
		for pregunta in self.examen.preguntas:
			print(f"Pregunta n° {i+1}: {pregunta}")
			print(f'Respuesta dada: {self.respuestas[i][0]}')
			print(f'Respuesta correcta: {pregunta.rta}')
			print(f'Puntaje: {self.respuestas[i][1]}')
			print('------------------------------------')
			i += 1


class Examen:
	def __init__(self, nombre=''):
		self.nombre = nombre
		self.preguntas = []

	def set_nombre(self):
		self.nombre = input("Ingrese el nombre del examen: ")

	def start(self):
		self.set_nombre()
		flag = True
		while flag:
			flag = self.menu()

	def menu(self):
		print("""OPCIONES
			1. Agregar pregunta
			2. Obtener pregunta
			3. Permutar pregunta
			4. Borrar pregunta
			5. Contiene pregunta
			6. Salir""")
		op = int(input())
		if op == 1:
			self.agregar_pregunta()
		elif op == 2:
			self.obtener_pregunta()
		elif op == 3:
			self.permutar_pregunta()
		elif op == 4:
			self.borrar_pregunta()
		elif op == 5:
			self.contiene_pregunta()
		elif op == 6:
			return False
		return True

	def agregar_pregunta(self):
		pregunta = Pregunta()
		pregunta.start()
		self.preguntas.append(pregunta)

	def obtener_pregunta(self):
		n = int(input("Ingrese el número de la pregunta que desea obtener: "))
		try:
			print(f'Pregunta número {n}: {self.preguntas[n-1]}')
		except IndexError:
			print(f"No hay una pregunta número {n}.")

	def existe_posicion(self, num):
		try:
			self.preguntas[num-1]
			return True
		except IndexError:
			return False

	def permutar_pregunta(self):
		n = int(input("Ingrese el número de pregunta que desea mover: "))
		nn = int(input(f"¿A qué lugar desea moverla? (Nota: Hay {len(self.preguntas)} preguntas): "))
		if self.existe_posicion(nn):
			pregunta = self.preguntas.pop(n-1)
			self.preguntas.insert(nn, pregunta)
			print("Operación realizada con éxito")
		else:
			print("No se pudo mover la pregunta a un lugar no existente.")

	def borrar_pregunta(self):
		print("""Cómo desea borrar?
			1. Por número de pregunta
			2. Por texto de pregunta""")
		op = int(input(">>"))
		if op == 1:
			n = int(input("Ingrese el número de la pregunta que desea borrar: "))
			preg = self.preguntas.pop(n-1)
			print(f"Operación exitosa. Se ha borrado la pregunta: {preg}")
		elif op == 2:
			st = input("Ingrese el texto de la pregunta\n>>")
			i = 0
			for pregunta in self.preguntas:
				if pregunta.texto.startswith(st):
					preg = self.preguntas.pop(i)
					print(f"Operación exitosa. Se ha borrado la pregunta número {i+1}")
				i += 1

	def contiene_pregunta(self):
		st = input("Ingrese el texto de la pregunta\n>>")
		for pregunta in self.preguntas:
			if pregunta.texto == st:
				print('True')
				return True
		print('False')
		return False


