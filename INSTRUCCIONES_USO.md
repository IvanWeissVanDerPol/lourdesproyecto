# 📚 PROYECTO DE INVESTIGACIÓN - GUÍA DE USO

## ✅ LO QUE TIENES AHORA

Tu proyecto está completamente organizado y funcional. Aquí está todo:

### 📂 Estructura de Carpetas

```
lourdes/
│
├── proyecto_secciones/              ← CARPETA PRINCIPAL DE TRABAJO
│   ├── 00_portada.md               (686 bytes)
│   ├── 01_indice.md                (4.1 KB)
│   ├── 02_resumen.md               (2.0 KB)
│   ├── 03_palabras_clave.md        (223 bytes)
│   ├── 04_introduccion.md          (4.2 KB)
│   ├── 05_politicas_institucionales.md (5.6 KB)
│   ├── 06_fundamentacion_teorica.md    (22 KB)
│   ├── 07_planteamiento_problema.md    (5.8 KB)
│   ├── 08_hipotesis.md             (5.7 KB)
│   ├── 09_objetivos.md             (6.3 KB)
│   ├── 10_variables.md             (22 KB) ← EXHAUSTIVO
│   ├── 11_metodologia.md           (34 KB) ← EXHAUSTIVO
│   ├── consolidar.py               ← Script rápido
│   ├── dividir_proyecto.py         ← Script completo
│   ├── extraer_secciones.py        ← Script extractor
│   └── README.md                   ← Instrucciones detalladas
│
├── PROYECTO_FINAL_CONSOLIDADO.md   ← DOCUMENTO COMPLETO (112 KB, 1,863 líneas)
├── PROYECTO_COMPLETO_FINAL.md      (Original parte 1)
├── PROYECTO_COMPLETO_FINAL_PARTE2.md (Original parte 2)
└── Plantillas/ (consentimientos, registros, etc.)
```

---

## 🚀 CÓMO TRABAJAR CON ESTO

### OPCIÓN 1: Editar Secciones Individualmente (RECOMENDADO) ⭐

**Para qué**: Cuando quieres editar o completar una sección específica

**Pasos**:
1. Abre la carpeta `proyecto_secciones`
2. Abre el archivo que quieres editar (ej: `14_cronograma.md`)
3. Edita el contenido
4. Guarda

**Ventajas**:
- ✅ Más fácil para trabajar en equipo
- ✅ Cada persona trabaja en su archivo
- ✅ No se estorban entre ustedes
- ✅ Más fácil ver qué falta

### OPCIÓN 2: Consolidar en Documento Único

**Para qué**: Cuando quieres ver TODO el proyecto junto o preparar entrega

**Pasos**:
1. Abre terminal/cmd en la carpeta `proyecto_secciones`
2. Ejecuta: `python consolidar.py`
3. Se crea/actualiza: `PROYECTO_FINAL_CONSOLIDADO.md`

**O simplemente**:
- Ya tienes el archivo `PROYECTO_FINAL_CONSOLIDADO.md` listo con todo lo actual

---

## 📊 ESTADO ACTUAL

### ✅ COMPLETADO (54% - 12/22 secciones)

| # | Sección | Estado | Tamaño |
|---|---------|--------|--------|
| 00 | Portada | ✅ Completa (falta solo llenar nombres) | 686 B |
| 01 | Índice | ✅ Completo | 4.1 KB |
| 02 | Resumen | ✅ Completo (247 palabras) | 2.0 KB |
| 03 | Palabras clave | ✅ Completo | 223 B |
| 04 | Introducción | ✅ Completa | 4.2 KB |
| 05 | Políticas Institucionales | ✅ Completa | 5.6 KB |
| 06 | Fundamentación Teórica | ✅ EXHAUSTIVA (antecedentes+marco+justificación) | 22 KB |
| 07 | Planteamiento del Problema | ✅ Completo | 5.8 KB |
| 08 | Hipótesis | ✅ Completas (5 específicas + nula) | 5.7 KB |
| 09 | Objetivos | ✅ Completos (1 general + 11 específicos) | 6.3 KB |
| 10 | Variables | ✅ EXHAUSTIVO (todas operacionalizadas) | 22 KB |
| 11 | Metodología | ✅ EXHAUSTIVA (diseño+participante+instrumentos+procedimiento) | 34 KB |

### ⏳ PENDIENTE (46% - 10/22 secciones)

| # | Sección | Responsable | Prioridad |
|---|---------|-------------|-----------|
| 12 | Estrategia de Implementación | Lourdes | 🔴 Alta |
| 13 | Descripción Sesiones | Lourdes | 🔴 Alta |
| 14 | Cronograma | Ayelen | 🔴 Alta |
| 15 | Presupuesto | Lourdes | 🔴 Alta |
| 16 | Aspectos Éticos | Miranda | 🔴 Alta |
| 17 | Análisis de Datos | Todas | 🔴 Alta |
| 18 | Resultados Esperados | Miranda | 🔴 Alta |
| 19 | Limitaciones | Ayelen | 🔴 Alta |
| 20 | Aportes | Miranda | 🔴 Alta |
| 21 | Referencias (APA 7) | Ayelen | 🔴 Alta |
| 22 | Anexos | Lourdes | 🟡 Media |

---

## 💡 PARA CADA SECCIÓN PENDIENTE

### 12. Estrategia de Implementación (Lourdes)

**Qué incluir**:
- Descripción del diseño de criterio cambiante
- Cómo se implementará fase por fase
- Cómo se evaluará el cumplimiento de criterios
- Estrategias para mantener motivación

**Archivo**: `proyecto_secciones/12_estrategia_implementacion.md`

### 13. Descripción de Sesiones (Lourdes)

**Qué incluir**:
- Protocolo detallado de cada sesión (minuto a minuto)
- Sesión 0 (línea base)
- Sesiones 1-4 (intervención con criterios 7, 10, 12, 15 min)
- Sesión 5 (post-evaluación)
- Guiones específicos de lo que se dirá
- Materiales necesarios por sesión

**Archivo**: `proyecto_secciones/13_descripcion_sesiones.md`

**NOTA**: La sección 11 (Metodología) ya tiene mucho de esto. Puedes copiar y expandir.

### 14. Cronograma (Ayelen)

**Qué incluir**:
- Tabla con fechas específicas
- Fases del proyecto (preparación, evaluación, intervención, análisis)
- Diagrama de Gantt (opcional)
- Asignación de responsabilidades por fecha

**Archivo**: `proyecto_secciones/14_cronograma.md`

**Ejemplo de tabla**:
```markdown
| Semana | Fechas | Actividad | Responsable |
|--------|--------|-----------|-------------|
| 0 | Nov 1-7 | Contacto con familia, consentimientos | Miranda |
| 1 | Nov 8-14 | Sesión 0 (línea base) | Todas |
| 2 | Nov 15-21 | Sesiones 1-2 | Lourdes |
```

### 15. Presupuesto (Lourdes)

**Qué incluir**:
- Tabla detallada de recursos necesarios
- Costos estimados
- Fuentes de financiamiento

**Archivo**: `proyecto_secciones/15_presupuesto.md`

**Ejemplo**:
```markdown
| Ítem | Cantidad | Costo Unitario | Total |
|------|----------|----------------|-------|
| Tests impresos | 3 juegos | Gs. 50,000 | Gs. 150,000 |
| Material didáctico | 1 set | Gs. 30,000 | Gs. 30,000 |
| Cronómetro | 1 | Gs. 15,000 | Gs. 15,000 |
| Regalo (botines) | 1 | Gs. 200,000 | Gs. 200,000 |
| **TOTAL** | | | **Gs. 395,000** |
```

### 16. Aspectos Éticos (Miranda)

**Qué incluir**:
- Principios éticos que guían el estudio
- Proceso de consentimiento informado (explicar el documento)
- Confidencialidad y protección de datos
- Protocolo de manejo de datos
- Consideraciones sobre el incentivo
- Derecho a retirarse
- Beneficencia y no maleficencia

**Archivo**: `proyecto_secciones/16_aspectos_eticos.md`

**Puedes basarte en**: `PLANTILLA_Consentimiento_Informado.md` y `PLANTILLA_Protocolo_Confidencialidad.md`

### 17. Plan de Análisis de Datos (Todas)

**Qué incluir**:
- Cómo se analizarán los datos de cada sesión
- Análisis visual de gráficas
- Comparación pre-post de WISC-5
- Análisis de criterio cambiante
- Software a usar (Excel, SPSS, análisis manual)
- Criterios para determinar si hipótesis se confirmaron

**Archivo**: `proyecto_secciones/17_analisis_datos.md`

### 18. Resultados Esperados (Miranda)

**Qué incluir**:
- Gráficas proyectadas (dibujar cómo se espera que se vean)
- Predicciones específicas vinculadas a hipótesis
- Tablas de resultados esperados (pre vs post)
- Interpretación de los resultados esperados
- Implicaciones si se confirman las hipótesis

**Archivo**: `proyecto_secciones/18_resultados_esperados.md`

### 19. Limitaciones (Ayelen)

**Qué incluir**:
- Limitaciones del diseño N=1 (no generalizable a población)
- Limitaciones de tiempo (solo 3 semanas)
- Limitaciones de recursos
- Posibles sesgos y cómo se controlaron
- Amenazas a la validez interna/externa

**Archivo**: `proyecto_secciones/19_limitaciones.md`

### 20. Aportes (Miranda)

**Qué incluir**:
- Aportes teóricos (llenar vacío en literatura)
- Aportes prácticos (protocolo replicable)
- Aportes sociales (accesibilidad, bajo costo)
- Aportes metodológicos (diseño N=1 en contexto local)
- Relevancia para políticas educativas
- Aplicabilidad a otros casos

**Archivo**: `proyecto_secciones/20_aportes.md`

### 21. Referencias (Ayelen)

**Qué incluir**:
- TODAS las referencias citadas en el texto
- Formato APA 7 correcto
- Ordenadas alfabéticamente
- Mínimo 20-25 referencias

**Archivo**: `proyecto_secciones/21_referencias.md`

**Formato APA 7**:
```markdown
American Psychiatric Association. (2013). *Diagnostic and statistical manual of mental disorders* (5th ed.). https://doi.org/10.1176/appi.books.9780890425596

Barkley, R. A. (2015). *Attention-deficit hyperactivity disorder: A handbook for diagnosis and treatment* (4th ed.). Guilford Press.

DuPaul, G. J., Eckert, T. L., & Vilardo, B. (2012). The effects of school-based interventions for attention deficit hyperactivity disorder: A meta-analysis 1996–2010. *School Psychology Review, 41*(4), 387-412.
```

### 22. Anexos (Lourdes)

**Qué incluir**:
- Anexo A: Consentimiento Informado (incluir plantilla completa)
- Anexo B: Protocolo de Confidencialidad
- Anexo C: Entrevista a Padres (plantilla completa)
- Anexo D: Registro de Sesiones (plantilla completa)
- Anexo E: Ejemplos de materiales académicos
- Anexo F: Lista de cotejo de fidelidad
- Anexo G: Cuestionario de psicohigiene

**Archivo**: `proyecto_secciones/22_anexos.md`

**Formato**:
```markdown
# 21. ANEXOS

## ANEXO A: Consentimiento Informado

[Copiar contenido completo de PLANTILLA_Consentimiento_Informado.md]

---

## ANEXO B: Protocolo de Confidencialidad

[Copiar contenido completo de PLANTILLA_Protocolo_Confidencialidad.md]

---

[etc.]
```

---

## 🎯 PLAN DE ACCIÓN RECOMENDADO

### SEMANA 1

**Lunes-Martes**:
- Lourdes: Secciones 12 y 13
- Ayelen: Sección 14 (cronograma)
- Miranda: Sección 16 (ética)

**Miércoles-Jueves**:
- Lourdes: Sección 15 (presupuesto)
- Ayelen: Sección 19 (limitaciones)
- Miranda: Sección 18 (resultados)

**Viernes**:
- Todas: Sección 17 (análisis de datos) juntas
- Miranda: Sección 20 (aportes)

### SEMANA 2

**Lunes-Miércoles**:
- Ayelen: Sección 21 (referencias) - llevar tiempo
- Lourdes: Sección 22 (anexos)

**Jueves**:
- Consolidar: `python consolidar.py`
- Revisar documento completo juntas

**Viernes**:
- Revisión cruzada
- Correcciones finales

### SEMANA 3

- Aplicar formato APA en Word
- Revisión final
- Entrega

---

## 🛠️ COMANDOS ÚTILES

### Consolidar proyecto
```bash
cd proyecto_secciones
python consolidar.py
```

### Ver estado
```bash
cd proyecto_secciones
python dividir_proyecto.py verificar
```

### Consolidar (alternativo)
```bash
cd proyecto_secciones
python dividir_proyecto.py consolidar
```

---

## 📞 AYUDA

**Problemas con scripts**:
- Verificar que Python esté instalado
- Ejecutar desde la carpeta correcta
- Leer mensajes de error

**Problemas de contenido**:
- Revisar README.md en proyecto_secciones
- Consultar secciones ya completadas como ejemplo
- Preguntar al profesor

**Problemas de formato**:
- Usar markdown básico
- Copiar estructura de secciones existentes
- Al final se aplica formato APA en Word

---

## ✅ VENTAJAS DE ESTE SISTEMA

1. ✅ **Trabajo en paralelo**: Cada una edita su archivo sin conflictos
2. ✅ **Fácil ver progreso**: Archivos completados vs faltantes
3. ✅ **Consolidación automática**: Un comando y tienes todo junto
4. ✅ **Control de versiones**: Fácil ver qué cambió en cada archivo
5. ✅ **Modular**: Fácil agregar/quitar/reorganizar secciones
6. ✅ **Respaldos**: Si algo sale mal, tienes cada sección por separado

---

## 🎓 CALIDAD DEL PROYECTO ACTUAL

Lo que ya tienen es de **nivel tesis de grado**:

- ✅ Marco teórico de 22 KB (exhaustivo)
- ✅ Metodología de 34 KB (detallada)
- ✅ Variables completamente operacionalizadas
- ✅ 25+ referencias citadas
- ✅ Diseño experimental riguroso
- ✅ Hipótesis específicas medibles
- ✅ 11 objetivos específicos con indicadores

**Con las 10 secciones restantes**, tendrán un proyecto COMPLETO y PROFESIONAL de aproximadamente 80-100 páginas.

---

## 🚀 ¡ADELANTE!

Tienen una excelente base. Las secciones pendientes son más cortas y directas que las ya completadas.

**Pueden hacerlo. Sigan el plan.** 💪

---

**Fecha**: Octubre 30, 2025
**Versión**: 1.0
