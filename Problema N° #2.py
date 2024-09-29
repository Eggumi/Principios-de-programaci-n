base_triangulo = float(input("Introduce la base del triángulo: "))
altura_triangulo = float(input("Introduce la altura del triángulo: "))

radio_circulo = float(input("Introduce el radio del círculo: "))

ancho_brazos = float(input("Introduce el ancho de los brazos: "))
altura_brazos = float(input("Introduce la altura de los brazos: "))

ancho_piernas = float(input("Introduce el ancho de las piernas: "))
altura_piernas = float(input("Introduce la altura de las piernas: "))

ancho_cuerpo = float(input("Introduce el ancho del cuerpo: "))
altura_cuerpo = float(input("Introduce la altura del cuerpo: "))

area_triangulo_total = (base_triangulo * altura_triangulo) / 2
area_circulo_total = (3.14 * radio_circulo**2)
area_brazos_total = ancho_brazos * altura_brazos
area_piernas_total = ancho_piernas * altura_piernas
area_cuerpo_total = ancho_cuerpo * altura_cuerpo

print("Área del triángulo: {area_triangulo_total: ")
print("Área del círculo: {area_circulo_total: ")
print("Área de los brazos: {area_brazos_total: ")
print("Área de las piernas: {area_piernas_total: ")
print("Área del cuerpo: {area_cuerpo_total: ")

area_total = area_triangulo_total+area_circulo_total+area_brazos_total+area_piernas_total+area_cuerpo_total

print(area_total)
