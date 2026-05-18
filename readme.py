# Sistema de Gestión de Servicios de Gimnasio

## Descripción del Proyecto
Este proyecto fue desarrollado en Python aplicando los principios de Programación Orientada a Objetos (POO).  
El sistema permite administrar servicios de gimnasio, membresías, entrenamientos personalizados y socios registrados, utilizando conceptos como:

- Herencia
- Encapsulamiento
- Polimorfismo
- Composición
- Métodos especiales (`__str__`)
- Getters y Setters con `@property`

El proyecto simula el funcionamiento básico de un gimnasio mediante un catálogo de servicios y la administración de socios.

---

# Integrantes
- Cevallos Mendoza Samantha Nikole
- Laura Fernanda Guillén Vargas
- Cristhian Isaac Estrella Espinoza
- Evelyn Noemi Burbano Mora
- Janeth Maria Verdezoto García

---

# Tecnologías Utilizadas
- Python 3
- Programación Orientada a Objetos (POO)
- GitHub
- Visual Studio Code / PyCharm

---

# Estructura del Proyecto

```bash
ProyectoGimnasio/
│── ClasePadre.py
│── ClaseHija1.py
│── ClaseHija2.py
│── Socio.py
│── GestorGimnasio.py
│── main.py
│── README.md
```

---

# Clases Implementadas

## Clase Base: ServicioGimnasio
Representa los servicios generales del gimnasio.

### Atributos
- código
- nombre
- descripción
- precio

### Métodos
- mostrar_servicio()
- aplicar_descuento()
- calcular_precio_anual()

### Conceptos aplicados
 Encapsulamiento  
 Getters y Setters  
 Polimorfismo

---

## Clase Hija 1: MembresiaMensual
Hereda de `ServicioGimnasio`.

Representa planes mensuales con promociones y duración específica.

### Atributos adicionales
- duración_meses
- promoción

### Métodos adicionales
- calcular_costo()
- generar_reporte()

### Conceptos aplicados
 Herencia  
 Polimorfismo  
 Encapsulamiento

---

## Clase Hija 2: EntrenamientoPersonalizado
Hereda de `ServicioGimnasio`.

Representa entrenamientos personalizados con entrenador asignado.

### Atributos adicionales
- entrenador
- sesiones_por_mes
- nivel

### Métodos adicionales
- precio_por_sesion()
- mostrar_servicio() → sobrescrito
- calcular_precio_anual() → sobrescrito

### Conceptos aplicados
 Herencia  
 Polimorfismo  
 Sobreescritura de métodos

---

##  Clase Adicional: Socio
Representa a un miembro registrado en el gimnasio.

### Atributos
- código_socio
- nombre
- email
- teléfono
- servicio activo

### Métodos
- mostrar_info()
- cambiar_servicio()

### Conceptos aplicados
 Composición  
 Encapsulamiento  
 Validaciones

---

##  Clase Adicional: GestorGimnasio
Administra el catálogo de servicios y los socios registrados.

### Funciones principales
- Agregar servicios
- Eliminar servicios
- Registrar socios
- Mostrar catálogo
- Calcular ingresos
- Reportes anuales

### Conceptos aplicados
 Gestión de objetos  
 Polimorfismo  
 Encapsulamiento

---

# Funcionalidades del Sistema
- Registro de servicios del gimnasio
- Registro de socios
- Gestión de membresías
- Gestión de entrenamientos personalizados
- Aplicación de descuentos
- Cálculo de precios anuales
- Reportes detallados
- Cambio de servicio de socios
- Administración general del gimnasio

---

# Conceptos de Programación Aplicados

| Concepto | Aplicación |
|---|---|
| Encapsulamiento | Uso de atributos privados |
| Herencia | Clases hijas derivadas de ServicioGimnasio |
| Polimorfismo | Métodos sobrescritos |
| Composición | Socio contiene un ServicioGimnasio |
| Abstracción | Organización modular de clases |

---

#  Ejecución del Proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/Samantha-Cevallos-crypto/Proyecto1ParcialGrupo2.git
```

## 2️. Entrar a la carpeta del proyecto

```bash
cd Proyecto1ParcialGrupo2
```

## 3️. Ejecutar el programa

```bash
python main.py
```

---

# Ejemplo de Salida

```bash
======= CATÁLOGO DE SERVICIOS =======

Código      : S001
Nombre      : Acceso Libre
Precio      : $30.00

══════ MEMBRESÍA MENSUAL ══════
Nombre            : Membresía Básica
Duración          : 3 meses
Costo total       : $121.50

══════ DATOS DEL SOCIO ══════
Nombre      : Laura Pérez
Servicio    : Membresía Básica
```

---

# Objetivo Académico
Este proyecto fue realizado con fines educativos para fortalecer conocimientos sobre Programación Orientada a Objetos, modelado de clases y desarrollo de sistemas utilizando Python.

---

# Repositorio del Proyecto
https://github.com/Samantha-Cevallos-crypto/Proyecto1ParcialGrupo2.git

---
#link del video explicativo
https://drive.google.com/drive/folders/1mtCHS0X_2V7wYFK5LqI_J2cnYgomMix1?usp=sharing
# Licencia
Proyecto de uso académico y educativo.
