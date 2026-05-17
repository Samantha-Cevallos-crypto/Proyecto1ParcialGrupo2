# Integrantes:
# - Cevallos Mendoza Samantha nikole
# - Laura Fernanda Guillén Vargas
# -Cristhian Isaac Estrella Espinoza
# -Evelyn Noemi Burbano Mora
# -Janeth Maria Verdezoto García

# ─────────────────────────────────────────────
#  IMPORTACIONES
# ─────────────────────────────────────────────
from ClasePadre       import ServicioGimnasio, procesar_servicios
from ClaseHija1       import MembresiaMensual
from Clasehija2     import EntrenamientoPersonalizado
from Socio            import Socio
from Gestorgimnasio   import GestorGimnasio


# ═══════════════════════════════════════════════════════════
#  1. OBJETOS DE LA CLASE BASE: ServicioGimnasio
# ═══════════════════════════════════════════════════════════
s1 = ServicioGimnasio("S001", "Acceso Libre",
                      "Uso ilimitado de máquinas", 30.00)

s2 = ServicioGimnasio("S002", "Spinning",
                      "Clase de ciclismo indoor", 15.00)


# ═══════════════════════════════════════════════════════════
#  2. OBJETOS DE CLASE HIJA 1: MembresiaMensual
# ═══════════════════════════════════════════════════════════
m1 = MembresiaMensual("M001", "Membresía Básica",
                      "Plan mensual con acceso general",
                      45.00, duracion_meses=3, promocion=10)

m2 = MembresiaMensual("M002", "Membresía Premium",
                      "Plan mensual con acceso completo y clases",
                      80.00, duracion_meses=6, promocion=15)


# ═══════════════════════════════════════════════════════════
#  3. OBJETOS DE CLASE HIJA 2: EntrenamientoPersonalizado
# ═══════════════════════════════════════════════════════════
ep1 = EntrenamientoPersonalizado(
    "EP001", "Plan Básico PT",
    "Entrenamiento personalizado nivel básico",
    120.00,
    entrenador="Carlos Mendoza",
    sesiones_por_mes=8,
    nivel="Básico"
)

ep2 = EntrenamientoPersonalizado(
    "EP002", "Plan Elite PT",
    "Entrenamiento personalizado nivel avanzado",
    280.00,
    entrenador="Ana Ríos",
    sesiones_por_mes=20,
    nivel="Avanzado"
)


# ═══════════════════════════════════════════════════════════
#  4. POLIMORFISMO: lista heterogénea de objetos
# ═══════════════════════════════════════════════════════════
catalogo = [s1, s2, m1, m2, ep1, ep2]

# procesar_servicios llama a los mismos métodos sobre objetos de distintas clases
procesar_servicios(catalogo)


# ═══════════════════════════════════════════════════════════
#  5. MÉTODOS PROPIOS DE CLASE HIJA 1: generar_reporte()
# ═══════════════════════════════════════════════════════════
print("\n======= REPORTE DETALLADO DE MEMBRESÍAS =======\n")
m1.generar_reporte()
m2.generar_reporte()


# ═══════════════════════════════════════════════════════════
#  6. __str__ de objetos de todas las clases
# ═══════════════════════════════════════════════════════════
print("\n======= REPRESENTACIÓN __str__ =======\n")
print(s1)
print(s2)
print(m1)
print(m2)
print(ep1)
print(ep2)


# ═══════════════════════════════════════════════════════════
#  7. CLASE ADICIONAL: Socio
# ═══════════════════════════════════════════════════════════
print("\n======= REGISTRO DE SOCIOS =======\n")

socio1 = Socio("SOC001", "Laura Pérez",
               "laura@email.com", "0991234567", m1)

socio2 = Socio("SOC002", "Diego Torres",
               "diego@email.com", "0987654321", ep1)

socio3 = Socio("SOC003", "María Salazar",
               "maria@email.com", "0976543210", m2)

socio1.mostrar_info()
socio2.mostrar_info()
socio3.mostrar_info()

# Demostración de setter: cambio de servicio
print("\n── Cambio de servicio de socio ──")
socio1.cambiar_servicio(ep2)
print(socio1)


# ═══════════════════════════════════════════════════════════
#  8. CLASE ADICIONAL: GestorGimnasio
# ═══════════════════════════════════════════════════════════
print("\n======= GESTOR DEL GIMNASIO =======\n")

gestor = GestorGimnasio("FitLife Gym")

# Agregar servicios al catálogo
for srv in catalogo:
    gestor.agregar_servicio(srv)

# Registrar socios
gestor.registrar_socio(socio1)
gestor.registrar_socio(socio2)
gestor.registrar_socio(socio3)

# Mostrar catálogo y socios
gestor.mostrar_catalogo()
gestor.mostrar_socios()

# Reportes con polimorfismo interno
gestor.reporte_precios_anuales()
gestor.calcular_ingresos_totales()

# __str__ del gestor
print(f"\n{gestor}")