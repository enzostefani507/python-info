tamaño_del_pez = input("Ingrese el tamaño del pez: \n'Normal' \n'Debajo de lo Normal' \n'Encima de lo Normal' \n'Sobredimensionado'\n")
if tamaño_del_pez == "Normal":
	print("Pez en buenas condiciones")
elif tamaño_del_pez == "por debajo de lo Normal":
	print("Pez con problemas de nutrición")
elif tamaño_del_pez == "un poco por encima de lo Normal":
	print("Pez con síntomas de organismo contaminado")
elif tamaño_del_pez == "sobredimensionado":
	print("Pez contaminado")
else:
	print("Entrada invalida")