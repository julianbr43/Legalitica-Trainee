def es_misma_persona(objeto_a, objeto_b):
    # Regla 1: Verificar si los nombres son iguales
    if objeto_a['nombre'] != objeto_b['nombre']:
        return False
    
    # Regla 2: Verificar si las cédulas son iguales
    if objeto_a['cedula'] != objeto_b['cedula']:
        return False
    
    # Regla 3: Si ambas reglas anteriores se cumplen, entonces son la misma persona
    return True

pass
objeto_a = {
'nombre': 'Juan Perez',
'cedula': '12345678'
}
objeto_b = {
'nombre': 'Juan Perez',
'cedula': '12345678'
}
objeto_c = {
'nombre': 'Ana Lopez',
'cedula': '98765432'
}
print(es_misma_persona(objeto_a, objeto_b)) # True
print(es_misma_persona(objeto_a, objeto_c)) # False