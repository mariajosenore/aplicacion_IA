"""
Ejercicio 1: Sistema de Descuentos
Objetivo: Crear un sistema que calcule descuentos basados en diferentes criterios
"""

print("=== SISTEMA DE DESCUENTOS ===")

# Solicitar información del cliente
nombre = input("Nombre del cliente: ").strip().title()
edad = int(input("Edad del cliente: "))
es_estudiante = input("¿Es estudiante? (s/n): ").lower() == 's'
es_miembro = input("¿Es miembro del club? (s/n): ").lower() == 's'
monto_compra = float(input("Monto de la compra: $"))

print(f"\n--- PROCESANDO DESCUENTOS PARA {nombre} ---")

# Inicializar variables de descuento
descuento_edad = 0
descuento_estudiante = 0
descuento_miembro = 0
descuento_monto = 0

# Descuento por edad
if edad >= 65:
    descuento_edad = 15  # 15% para adultos mayores
    print(f"✓ Descuento adulto mayor: {descuento_edad}%")
elif edad < 18:
    descuento_edad = 10  # 10% para menores
    print(f"✓ Descuento menor de edad: {descuento_edad}%")

# Descuento por ser estudiante
if es_estudiante:
    descuento_estudiante = 12  # 12% para estudiantes
    print(f"✓ Descuento estudiante: {descuento_estudiante}%")

# Descuento por membresía
if es_miembro:
    descuento_miembro = 8  # 8% para miembros
    print(f"✓ Descuento miembro del club: {descuento_miembro}%")

# Descuento por monto de compra
if monto_compra >= 1000:
    descuento_monto = 20  # 20% para compras grandes
    print(f"✓ Descuento compra mayor a $1000: {descuento_monto}%")
elif monto_compra >= 500:
    descuento_monto = 10  # 10% para compras medianas
    print(f"✓ Descuento compra mayor a $500: {descuento_monto}%")
elif monto_compra >= 200:
    descuento_monto = 5  # 5% para compras pequeñas
    print(f"✓ Descuento compra mayor a $200: {descuento_monto}%")

# Calcular descuento total (máximo 50%)
descuento_total = min(
    descuento_edad + descuento_estudiante + descuento_miembro + descuento_monto, 
    50
)

# Calcular montos finales
monto_descuento = monto_compra * (descuento_total / 100)
monto_final = monto_compra - monto_descuento

# Mostrar resumen
print("\n=== RESUMEN DE DESCUENTOS ===")
print(f"Cliente: {nombre}")
print(f"Monto original: ${monto_compra:.2f}")
print(f"Descuento total aplicado: {descuento_total}%")
print(f"Total descuento: ${monto_descuento:.2f}")
print(f"Total a pagar: ${monto_final:.2f}")
