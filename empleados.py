def pedir_datos():
    empleados = []
    n = int(input("¿Cuántos empleados desea agregar? "))
    for i in range(n):
        print(f"\nIngrese los datos del empleado {i + 1}:")
        nombre = input("Nombre: ").strip()
        estado_civil = input("Estado civil: ").strip()
        antiguedad = int(input("Antigüedad (años): ").strip())
        categoria = input("Categoría: ").strip()
        sueldo = float(input("Sueldo: ").strip())
        empleados.append({
            "nombre": nombre,
            "estado_civil": estado_civil,
            "antigüedad": antiguedad,
            "categoría": categoria,
            "sueldo": sueldo
        })
    return empleados

def mezcla_directa(lista):
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    izquierda = mezcla_directa(lista[:mitad])
    derecha = mezcla_directa(lista[mitad:])
    
    return mezclar(izquierda, derecha)

def mezcla_equilibrada(lista):
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    izquierda = mezcla_equilibrada(izquierda)
    derecha = mezcla_equilibrada(derecha)
    
    return mezclar(izquierda, derecha)

def mezclar(izquierda, derecha):
    resultado = []
    estado_civil_map = {'C': 0, 'S': 1, 'D': 2}

    while izquierda and derecha:
        if (izquierda[0]["nombre"] < derecha[0]["nombre"]) or \
           (izquierda[0]["nombre"] == derecha[0]["nombre"] and izquierda[0]["antigüedad"] > derecha[0]["antigüedad"]) or \
           (izquierda[0]["nombre"] == derecha[0]["nombre"] and izquierda[0]["antigüedad"] == derecha[0]["antigüedad"] and izquierda[0]["sueldo"] > derecha[0]["sueldo"]) or \
           (izquierda[0]["nombre"] == derecha[0]["nombre"] and 
            izquierda[0]["antigüedad"] == derecha[0]["antigüedad"] and 
            izquierda[0]["sueldo"] == derecha[0]["sueldo"] and 
            estado_civil_map[izquierda[0]["estado_civil"]] < estado_civil_map[derecha[0]["estado_civil"]]):
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))

    resultado.extend(izquierda)
    resultado.extend(derecha)
    
    return resultado

def mostrar_empleados(empleados):
    print("\nEmpleados ordenados:")
    for emp in empleados:
        print(f"{emp['nombre']:10} | {emp['estado_civil']:10} | {emp['antigüedad']:5} | {emp['categoría']:5} | {emp['sueldo']:10.2f}")

print("Ordenación de empleados por nombre, antigüedad, sueldo y estado civil en caso de empate")
empleados = pedir_datos()

print("\nOrdenando por mezcla directa...")
ordenados_directa = mezcla_directa(empleados)
mostrar_empleados(ordenados_directa)

print("\nOrdenando por mezcla equilibrada...")
ordenados_equilibrada = mezcla_equilibrada(empleados)
mostrar_empleados(ordenados_equilibrada)
