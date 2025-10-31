# 📚 DOCUMENTACIÓN: CONVERTIDOR MARKDOWN → DOCX CON FORMATO APA 7

> **Convertidor completo con implementación correcta de todos los estándares APA 7ª edición**

---

## 🎯 CARACTERÍSTICAS

### ✅ Implementación Completa APA 7

1. **Portada**
   - ✅ Portada profesional (con running head)
   - ✅ Portada estudiantil (sin running head)
   - ✅ Numeración correcta desde página 1

2. **Formato de Documento**
   - ✅ Márgenes: 1 pulgada (2.54 cm) todos los lados
   - ✅ Fuente: Times New Roman 12pt
   - ✅ Interlineado: Doble en todo el documento
   - ✅ Sangría: 0.5 pulgadas (1.27 cm) primera línea
   - ✅ Alineación: Izquierda (no justificada)
   - ✅ Papel: Carta (8.5 × 11 pulgadas)

3. **Encabezados**
   - ✅ Nivel 1: Centrado, Negrita, Title Case
   - ✅ Nivel 2: Izquierda, Negrita, Title Case
   - ✅ Nivel 3: Izquierda, Negrita + Cursiva, Title Case
   - ✅ Nivel 4: Sangría, Negrita + Cursiva, Title Case, Punto
   - ✅ Nivel 5: Sangría, Negrita + Cursiva, Sentence case, Punto

4. **Elementos Especiales**
   - ✅ Resumen/Abstract (sin sangría, 150-250 palabras)
   - ✅ Palabras clave (con sangría, en cursiva)
   - ✅ Referencias (con sangría francesa de 0.5 pulgadas)
   - ✅ Citas en bloque (40+ palabras, sangría 0.5 pulgadas)

5. **Tablas**
   - ✅ Número de tabla (Tabla 1, en negrita)
   - ✅ Título de tabla (en cursiva)
   - ✅ Solo líneas horizontales (superior, inferior, entre encabezado)
   - ✅ Sin bordes verticales

6. **Figuras** (preparado para implementación)
   - Número de figura
   - Título de figura
   - Formato APA completo

---

## 📥 INSTALACIÓN

### Requisitos

```bash
pip install python-docx
```

### Versión de Python
- Python 3.7 o superior

---

## 🚀 USO BÁSICO

### Ejemplo 1: Documento Estudiantil

```python
from convertidor_apa7_completo import ConvertidorAPA7

# Crear convertidor
convertidor = ConvertidorAPA7(tipo_documento='estudiantil')

# Agregar portada
convertidor.agregar_portada(
    titulo="Título de tu Trabajo en Formato Title Case",
    autor="Tu Nombre Completo",
    institucion="Nombre de tu Universidad",
    departamento="Facultad de Psicología",
    curso="PSI-401: Metodología de Investigación",
    profesor="Prof. Dr. Nombre del Profesor",
    fecha="15 de octubre de 2025"
)

# Agregar resumen (opcional)
convertidor.agregar_resumen(
    texto_resumen="Este estudio investigó... (150-250 palabras)",
    palabras_clave=["palabra1", "palabra2", "palabra3", "palabra4"]
)

# Procesar archivo Markdown
convertidor.procesar_markdown("mi_documento.md")

# Guardar
convertidor.guardar("mi_documento_apa7.docx")
```

### Ejemplo 2: Documento Profesional

```python
from convertidor_apa7_completo import ConvertidorAPA7

# Crear convertidor profesional
convertidor = ConvertidorAPA7(tipo_documento='profesional')

# Agregar portada profesional
convertidor.agregar_portada(
    titulo="Título Completo del Artículo Científico",
    autor="Nombre Apellido",
    institucion="Universidad Nacional",
    departamento="Departamento de Psicología",
    running_head="TÍTULO ABREVIADO",  # Max 50 caracteres
    nota_autor="""Nombre Apellido, Departamento de Psicología, Universidad Nacional.

Esta investigación fue financiada por la Beca de Investigación XYZ.

El autor declara no tener conflictos de interés.

Correspondencia: nombre.apellido@universidad.edu""",
    tipo='profesional'
)

# Agregar resumen
convertidor.agregar_resumen(
    texto_resumen="El presente estudio...",
    palabras_clave=["atención", "intervención", "niños", "TDA"]
)

# Procesar contenido
convertidor.procesar_markdown("articulo.md")

# Guardar
convertidor.guardar("articulo_apa7.docx")
```

---

## 📝 FORMATO MARKDOWN SOPORTADO

### Encabezados

```markdown
## Nivel 1 (Centrado, Negrita)

### Nivel 2 (Izquierda, Negrita)

#### Nivel 3 (Izquierda, Negrita + Cursiva)

##### Nivel 4 (Sangría, Negrita + Cursiva, Punto)

###### Nivel 5 (Sangría, Negrita + Cursiva, Sentence case, Punto)
```

### Formato Inline

```markdown
**Texto en negrita**

*Texto en cursiva*

***Texto en negrita y cursiva***

`Código o término técnico`
```

### Listas

```markdown
- Lista con viñetas
- Segundo elemento
- Tercer elemento

1. Lista numerada
2. Segundo elemento
3. Tercer elemento
```

### Citas en Bloque

```markdown
> Este es un texto citado que se formateará como cita en bloque
> con sangría de 0.5 pulgadas según APA 7.
```

### Tablas

```markdown
**Tabla 1**
Título de la Tabla en Cursiva

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
|--------------|--------------|--------------|
| Dato 1       | Dato 2       | Dato 3       |
| Dato 4       | Dato 5       | Dato 6       |
```

**Nota**: El número de tabla se detecta automáticamente si usas `**Tabla X**` antes de la tabla.

### Código

````markdown
```
Bloque de código
que se formateará con fuente monoespaciada
```
````

### Sección de Referencias

```markdown
## Referencias

Apellido, A. A. (Año). Título del libro en cursiva. Editorial.

Apellido, B. B., & Apellido, C. C. (Año). Título del artículo. Revista en Cursiva, vol(núm), páginas. https://doi.org/xxx
```

**Nota**: La sangría francesa se aplica automáticamente a todo lo que esté después del encabezado "Referencias".

---

## 🎛️ PARÁMETROS DE LA CLASE

### ConvertidorAPA7(tipo_documento='estudiantil')

**Parámetros:**
- `tipo_documento` (str): 'estudiantil' o 'profesional'
  - Define el formato de portada y si se usa running head

---

## 📄 MÉTODO: agregar_portada()

### Parámetros Requeridos

```python
agregar_portada(
    titulo: str,        # Título completo del trabajo
    autor: str,         # Nombre del autor
    institucion: str,   # Nombre de la institución
    **kwargs           # Parámetros opcionales
)
```

### Parámetros Opcionales (kwargs)

| Parámetro | Tipo | Descripción | Uso |
|-----------|------|-------------|-----|
| `tipo` | str | 'profesional' o 'estudiantil' | Ambos |
| `running_head` | str | Título abreviado (max 50 caracteres, MAYÚSCULAS) | Solo profesional |
| `departamento` | str | Departamento o facultad | Ambos |
| `curso` | str | Código y nombre del curso | Solo estudiantil |
| `profesor` | str | Nombre del profesor/director | Solo estudiantil |
| `fecha` | str | Fecha de entrega | Estudiantil |
| `nota_autor` | str | Nota del autor con info de contacto | Solo profesional |

### Ejemplos

#### Portada Estudiantil Completa

```python
convertidor.agregar_portada(
    titulo="Efectos de la Meditación Mindfulness en la Reducción del Estrés",
    autor="María García López",
    institucion="Universidad Nacional",
    departamento="Facultad de Psicología",
    curso="PSI-450: Tesis de Licenciatura",
    profesor="Director de Tesis: Dr. Juan Pérez",
    fecha="30 de noviembre de 2025",
    tipo='estudiantil'
)
```

#### Portada Profesional Completa

```python
convertidor.agregar_portada(
    titulo="Efectividad de Intervenciones Basadas en Mindfulness para el Tratamiento del Estrés Laboral: Un Metaanálisis",
    autor="María García López y Juan Pérez Martínez",
    institucion="Universidad Nacional",
    departamento="Departamento de Psicología Clínica",
    running_head="MINDFULNESS Y ESTRÉS LABORAL",
    nota_autor="""María García López, Departamento de Psicología Clínica, Universidad Nacional; Juan Pérez Martínez, Instituto de Investigación en Salud Mental.

Este estudio fue financiado por la Beca de Investigación Científica #12345 del Consejo Nacional de Ciencia y Tecnología.

Los autores declaran no tener conflictos de interés.

Correspondencia: maria.garcia@universidad.edu""",
    tipo='profesional'
)
```

---

## 📄 MÉTODO: agregar_resumen()

### Parámetros

```python
agregar_resumen(
    texto_resumen: str,           # Texto del resumen (150-250 palabras)
    palabras_clave: list o str    # Lista de palabras clave (3-5)
)
```

### Ejemplo

```python
convertidor.agregar_resumen(
    texto_resumen="""El presente estudio investigó los efectos de una intervención basada en meditación mindfulness en la reducción del estrés laboral. Participaron 120 trabajadores de oficina divididos aleatoriamente en grupo experimental (n=60) y grupo control (n=60). El grupo experimental practicó meditación mindfulness durante 8 semanas con sesiones de 30 minutos diarios. Los resultados mostraron una reducción significativa del estrés en el grupo experimental (M=15.3, DE=4.2) comparado con el grupo control (M=28.7, DE=5.1), t(118)=15.67, p<.001. Se concluye que la meditación mindfulness es una intervención efectiva para reducir el estrés laboral.""",
    palabras_clave=["meditación mindfulness", "estrés laboral", "intervención", "trabajadores"]
)
```

O con lista:

```python
convertidor.agregar_resumen(
    texto_resumen="...",
    palabras_clave=[
        "meditación mindfulness",
        "estrés laboral",
        "intervención psicológica",
        "trabajadores de oficina",
        "salud mental"
    ]
)
```

---

## 📄 MÉTODO: procesar_markdown()

### Parámetro

```python
procesar_markdown(
    archivo_md: str    # Ruta al archivo Markdown
)
```

### Ejemplo

```python
convertidor.procesar_markdown("C:/Users/Usuario/Documentos/tesis.md")
```

---

## 📄 MÉTODO: guardar()

### Parámetro

```python
guardar(
    ruta: str    # Ruta donde guardar el archivo DOCX
)
```

### Ejemplo

```python
convertidor.guardar("C:/Users/Usuario/Documentos/tesis_apa7.docx")
```

---

## 🎨 ESTILOS DISPONIBLES

El convertidor crea automáticamente los siguientes estilos:

| Estilo | Nombre en Word | Uso |
|--------|---------------|-----|
| Normal | Normal | Texto del cuerpo |
| Heading 1 | Heading 1 | Encabezado Nivel 1 |
| Heading 2 | Heading 2 | Encabezado Nivel 2 |
| Heading 3 | Heading 3 | Encabezado Nivel 3 |
| Heading 4 | Heading 4 | Encabezado Nivel 4 |
| Heading 5 | Heading 5 | Encabezado Nivel 5 |
| Quote | Quote | Citas en bloque |
| Reference | Reference | Entradas de referencias |
| Abstract | Abstract | Texto del resumen |
| Table Title | Table Title | Títulos de tablas |
| Table Number | Table Number | Números de tablas |

---

## 🔧 PERSONALIZACIÓN

### Cambiar Tipo de Letra

Editar en `crear_estilos_apa7()`:

```python
# Cambiar de Times New Roman a Calibri 11pt
normal.font.name = 'Calibri'
normal.font.size = Pt(11)
```

### Cambiar Interlineado

```python
normal.paragraph_format.line_spacing = 1.5  # En lugar de 2.0
```

### Cambiar Márgenes

```python
section.top_margin = Inches(1.5)  # En lugar de 1
```

---

## ⚠️ LIMITACIONES ACTUALES

1. **Figuras**: Detección y formato automático no completamente implementado
2. **Apéndices**: No hay estilo específico (se procesan como texto normal)
3. **Notas de tabla**: No se detectan automáticamente
4. **Citas bibliográficas**: No se validan según formato APA
5. **Nivel 4 y 5**: El texto que continúa en la misma línea debe agregarse manualmente

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Problema: Encoding incorrecto (caracteres raros)

**Solución**: El archivo Markdown debe estar en UTF-8. Guardar como:
```python
with open('archivo.md', 'w', encoding='utf-8') as f:
    f.write(contenido)
```

### Problema: Tablas no se formatean correctamente

**Solución**: Asegurar que las tablas en Markdown tengan el formato correcto:
```markdown
| Col1 | Col2 |
|------|------|
| A    | B    |
```

### Problema: Running head no aparece

**Solución**: Asegurar que:
1. `tipo_documento='profesional'` al crear el convertidor
2. `running_head` se pasa como parámetro en `agregar_portada()`
3. El running head tiene máximo 50 caracteres

### Problema: Sangría francesa no se aplica a referencias

**Solución**: Asegurar que hay un encabezado `## Referencias` en el Markdown.

---

## 📊 COMPARACIÓN CON CÓDIGO ORIGINAL

| Característica | Código Original | Código Mejorado |
|----------------|----------------|-----------------|
| Niveles de encabezados | 4 niveles | 5 niveles ✅ |
| Running head | No | Sí (profesional) ✅ |
| Portada estudiantil vs profesional | No diferencia | Diferencia ✅ |
| Sangría francesa referencias | No | Sí ✅ |
| Resumen/Abstract | No | Sí ✅ |
| Palabras clave | No | Sí ✅ |
| Tablas APA | Parcial | Completo ✅ |
| Número y título de tabla | No | Sí ✅ |
| Numeración automática páginas | Manual | Automática ✅ |
| Bordes de tabla | Todos | Solo horizontales ✅ |
| Space before/after encabezados | Sí (incorrecto) | No (correcto) ✅ |

---

## 📚 REFERENCIAS

- American Psychological Association. (2020). *Publication manual of the American Psychological Association* (7th ed.). https://doi.org/10.1037/0000165-000

- Purdue OWL: https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/general_format.html

- APA Style: https://apastyle.apa.org/

---

## 🔄 VERSIONES

### v4.0 (Actual)
- ✅ Implementación completa de 5 niveles de encabezados
- ✅ Portada profesional y estudiantil
- ✅ Running head para documentos profesionales
- ✅ Resumen/Abstract con palabras clave
- ✅ Sangría francesa automática para referencias
- ✅ Tablas con formato APA completo
- ✅ Numeración automática de páginas
- ✅ Todos los estilos APA 7 correctos

### v3.0 (Anterior)
- Implementación parcial
- 4 niveles de encabezados
- Portada básica
- Tablas básicas

---

## 📞 SOPORTE

Para reportar problemas o sugerir mejoras:
- Revisar esta documentación primero
- Consultar las guías oficiales de APA 7
- Verificar que el archivo Markdown esté correctamente formateado

---

## 📝 EJEMPLO COMPLETO

```python
from convertidor_apa7_completo import ConvertidorAPA7

# 1. Crear convertidor
convertidor = ConvertidorAPA7(tipo_documento='estudiantil')

# 2. Agregar portada
convertidor.agregar_portada(
    titulo="Título del Trabajo en Formato Title Case",
    autor="Nombre del Estudiante",
    institucion="Universidad Nacional",
    departamento="Facultad de Psicología",
    curso="Tesis de Licenciatura",
    profesor="Director: Dr. Nombre Apellido",
    fecha="Octubre 2025"
)

# 3. Agregar resumen (opcional)
convertidor.agregar_resumen(
    texto_resumen="El estudio investigó... (150-250 palabras)",
    palabras_clave=["palabra1", "palabra2", "palabra3"]
)

# 4. Procesar Markdown
convertidor.procesar_markdown("mi_tesis.md")

# 5. Guardar
convertidor.guardar("mi_tesis_apa7.docx")

print("✅ Documento APA 7 creado exitosamente!")
```

---

**Versión**: 4.0
**Fecha**: Octubre 2025
**Basado en**: APA 7ª edición (2020)
**Estado**: Completamente funcional ✅
