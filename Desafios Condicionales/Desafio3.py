compuesto = float(input("Ingrese el abarcamieno del compuesto por hectarea - en porcentaje: "))
tipo_vegetacion = input("Ingrese tipo de vegetacion: ")
tipo_vegetacion = tipo_vegetacion.upper()
if tipo_vegetacion!="MATORRAL":
    no_existe_vegetación_tipo_matorral = True

if (compuesto<10.00) and no_existe_vegetación_tipo_matorral:
    print("Es factible utilizar ferilizantes")
else:
    print("No es factible utilizar fertilizantes")