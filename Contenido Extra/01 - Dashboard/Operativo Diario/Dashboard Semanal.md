# 🏠 Home - Centro de Comando Personal

> [!tip] 🌟 Bienvenido a tu Sistema de Conocimiento Este es tu punto de entrada principal. Desde aquí puedes acceder a todas las áreas de tu vida personal y profesional de manera organizada y eficiente.

>[!success] Siempre recuerda esto
>“Lo que me gusta no es un capricho, es **una brújula**.  
>Puede que hoy camine lento, pero sé exactamente hacia dónde voy.”
## 📅 Hoy es: `= date(now)`

>[!info] ⚡Estado Actual del Sistema
>**Última actualización:** `$= moment().format("h:mm a - MMMM DD, YYYY")`
>**Notas en el vault:** `$= dv.pages().length`
>**Enlaces totales:** En construcción
>**Próxima revisión:** Domingo

---
## Tracking Diario 🎯
>[!success] ✅ Tracking Diario **Semana del:** `$= moment().startOf('week').format('DD [de] MMMM YYYY')`
>
>⚠️ **Meditación (15 min):**
>
>- [ ] **Lunes**
>- [ ] **Martes**
>- [ ] **Miércoles**
>- [ ] **Jueves**
>- [ ] **Viernes**
>- [ ] **Sábado**
>- [ ] **Domingo**
>
🟢 **Estudio Enfocado (2h):**
>
>- [ ] **Lunes**
>- [ ] **Martes**
>- [ ] **Miércoles**
>- [ ] **Jueves**
>- [ ] **Viernes**
>- [ ] **Sábado**
>- [ ] **Domingo**
>
💪 **Ejercicio (30 min):**
>
>- [ ] **Lunes**
>- [ ] **Martes**
>- [ ] **Miércoles**
>- [ ] **Jueves**
>- [ ] **Viernes**
>- [ ] **Sábado**
>- [ ] **Domingo**
>
😴 **Sueño 8h (23:00-07:00):**
>
>- [ ] **Lunes**
>- [ ] **Martes**
>- [ ] **Miércoles**
>- [ ] **Jueves**
>- [ ] **Viernes**
>- [ ] **Sábado**
>- [ ] **Domingo**
>
>📱 **Detox Digital (1h antes de dormir):**
>
>- [ ] **Lunes**
>- [ ] **Martes**
>- [ ] **Miércoles**
>- [ ] **Jueves**
>- [ ] **Viernes**
>- [ ] **Sábado**
>- [ ] **Domingo**

---

>[!info] 📊 **Progreso Automático de la Semana**
>
>- **Meditación:** `$= dv.current().file.tasks.where(t => t.text.includes("Lunes") && t.text.includes("Meditación") || t.text.includes("Martes") && t.text.includes("Meditación")).where(t => t.completed).length`/7 días
>- **Estudio:** `$= Math.round((dv.current().file.tasks.where(t => t.completed && t.text.includes("Estudio")).length / 7) * 100)`% completado
>- **Ejercicio:** `$= Math.round((dv.current().file.tasks.where(t => t.completed && t.text.includes("Ejercicio")).length / 7) * 100)`% completado
>- **Sueño:** `$= Math.round((dv.current().file.tasks.where(t => t.completed && t.text.includes("Sueño")).length / 7) * 100)`% completado
>- **Detox Digital:** `$= Math.round((dv.current().file.tasks.where(t => t.completed && t.text.includes("Detox")).length / 7) * 100)`% completado
>
**Progreso Total:** `$= Math.round((dv.current().file.tasks.where(t => t.completed).length / dv.current().file.tasks.length) * 100)`%

---

>[!tip] 💡 **Cómo usar este tracker:**
>
>1. **Cada día:** Marca las casillas de los hábitos que completaste
>2. **Click directo:** Simplemente haz clic en cada checkbox ☐ para marcarlo ☑️
>3. **Progreso automático:** Se calcula solo en la sección de arriba
>4. **Nueva semana:** Copia esta plantilla y resetea todas las casillas

---

>[!tips] 🎯 **Metas de la Semana**
>
>- [ ] No saltarse más de 1 día de ejercicio
>- [ ] Dormir 8h mínimo 6/7 noches
>- [ ] Detox digital todas las noches

---

## 📝 **Notas y Reflexiones**

### ✅ **Éxitos de la semana:** 

### 🔄 **Áreas de mejora:**

### 💡 **Ajustes para próxima semana:**

---

## 🗓️ **Plantilla para próxima semana:**

```markdown
## ⚠️ **Meditación (15 min):**
- [ ] **Lunes** - [ ] **Martes** - [ ] **Miércoles** - [ ] **Jueves** - [ ] **Viernes** - [ ] **Sábado** - [ ] **Domingo**

## 🟢 **Estudio Enfocado (2h):**
- [ ] **Lunes** - [ ] **Martes** - [ ] **Miércoles** - [ ] **Jueves** - [ ] **Viernes** - [ ] **Sábado** - [ ] **Domingo**

## 💪 **Ejercicio (30 min):**
- [ ] **Lunes** - [ ] **Martes** - [ ] **Miércoles** - [ ] **Jueves** - [ ] **Viernes** - [ ] **Sábado** - [ ] **Domingo**

## 😴 **Sueño 8h (23:00-07:00):**
- [ ] **Lunes** - [ ] **Martes** - [ ] **Miércoles** - [ ] **Jueves** - [ ] **Viernes** - [ ] **Sábado** - [ ] **Domingo**

## 📱 **Detox Digital (1h antes de dormir):**
- [ ] **Lunes** - [ ] **Martes** - [ ] **Miércoles** - [ ] **Jueves** - [ ] **Viernes** - [ ] **Sábado** - [ ] **Domingo**
```

---

*Última actualización: `$= moment().format('DD [de] MMMM YYYY, HH:mm')`*
## 🎯 Objetivos de la Semana

> [!warning] 📋 Enfoque Semanal **Semana del:** _27 de Julio 2025_
> 
> ### 🏆 Objetivos Principales:
> 
> - [ ] **Productividad:** Implementar técnica de time-blocking
> - [ ] **Aprendizaje:** Completar revisión de método Feynman
> - [ ] **Bienestar:** Establecer rutina de sueño consistente
> - [ ] **Espacios:** Organizar escritorio según Feng Shui
> - [ ] **Digital:** Realizar audit de tiempo en pantalla


---

## 🗺️ Navegación Rápida

### 📁 Áreas Principales

> [!tip] 🚀 Acceso Directo a Carpetas
> 
> ```
> ┌─ 💼 PRODUCTIVIDAD
> │  ├─ [[Productividad Personal]]
> │  ├─ [[Deep Work]]
> │  ├─ [[Gestión del Tiempo]]
> │  └─ [[Bullet Journal Method (BuJo)]]
> │
> ├─ 🧠 APRENDIZAJE  
> │  ├─ [[Método 1 - Pomodoro]]
> │  ├─ [[Método 5 - Mapas Mentales]]
> │  ├─ [[Técnicas de Concentración]]
> │  └─ [[Neurociencia del Aprendizaje]]
> │
> ├─ 🌱 BIENESTAR
> │  ├─ [[Mindfulness]]
> │  ├─ [[Gestión del Estrés]]
> │  └─ [[Hábitos y Rutinas Saludables]]
> │
> ├─ 🏠 ESPACIOS
> │  ├─ [[Organización Física del Espacio]]
> │  ├─ [[Feng Shui para Espacios Pequeños]]
> │  └─ [[Minimismo Digital]]
> │
> └─ 💻 TECNOLOGÍA
>    ├─ [[Productividad Digital]]
>    └─ [[Detox Digital]]
> ```

### ⚡ Enlaces de Uso Frecuente

> [!info] 🔗 Accesos Directos **📊 Control y Seguimiento:**
> 
> - [[Dashboard Semanal]] - Revisión y planificación semanal
> - [[Tracking de Hábitos]] - Seguimiento detallado de hábitos
> - [[Objetivos 2026]] - Metas anuales y progreso
> 
> **🎯 Métodos Favoritos:**
> 
> - [[Método 1 - Pomodoro]] - Técnica de concentración
> - [[Deep Work]] - Trabajo profundo sin distracciones
> - [[Mindfulness]] - Práctica de atención plena
> 
> **📚 Recursos de Consulta:**
> 
> - [[Método 2 - Feynman]] - Aprender enseñando
> - [[Gestión del Estrés]] - Técnicas de manejo del estrés
> - [[Organización Física del Espacio]] - Optimización del entorno

---

## 📈 Panel de Progreso

### 🎯 Objetivos Anuales 2025

> [!success] 🏆 Progreso de Metas Principales **📚 Aprendizaje:**
> 
> - [ ] Dominar 10 métodos de estudio _(Progreso: 10/10 métodos documentados)_
> - [ ] Implementar sistema de repetición espaciada
> - [ ] Crear rutina de lectura diaria _(Meta: 30 min/día)_
> 
> **⚡ Productividad:**
> 
> - [ ] Establecer sistema GTD completo
> - [ ] Optimizar rutinas matutinas y nocturnas
> - [ ] Reducir tiempo en redes sociales 50%
> 
> **🌱 Bienestar:**
> 
> - [ ] Mantener práctica de meditación diaria _(Meta: 15 min)_
> - [ ] Optimizar calidad del sueño _(Meta: 8h consistentes)_
> - [ ] Integrar ejercicio regular _(Meta: 4x/semana)_
> 
> **🏠 Espacios:**
> 
> - [ ] Aplicar principios Feng Shui en todo el hogar
> - [ ] Crear espacio de trabajo ergonómico
> - [ ] Mantener organización según método KonMari

### 📊 Métricas Clave

> [!info] 📈 KPIs Personales **Esta Semana:**
> 
> - **Tiempo de estudio:** 0h / 10h objetivo
> - **Sesiones de deep work:** 0 / 5 objetivo
> - **Días sin estrés alto:** 0 / 5 objetivo
> - **Calidad del sueño:** Promedio pendiente
> - **Tiempo en pantalla:** Promedio pendiente

---

## 🔥 Área de Enfoque Actual

> [!warning] 🎯 Sprint de 30 Días **Tema del Mes:** Establecimiento de Rutinas Fundamentales
> 
> ### 🚀 Proyectos Activos:
> 
> 1. **Rutina Matutina Perfecta** _(Semana 1-2)_
>     - Despertar a las 6:00 AM consistentemente
>     - Secuencia: Meditación → Ejercicio → Planificación
>     - Integrar técnicas de [[Hábitos y Rutinas Saludables]]
> 2. **Optimización del Espacio de Trabajo** _(Semana 2-3)_
>     - Aplicar principios de [[Feng Shui para Espacios Pequeños]]
>     - Mejorar [[Organización Física del Espacio]]
>     - Crear zona de deep work libre de distracciones
> 3. **Sistema de Aprendizaje Integrado** _(Semana 3-4)_
>     - Combinar [[Método 1 - Pomodoro]] + [[Método 5 - Mapas Mentales]]
>     - Implementar revisión espaciada con [[Curva del Olvido]]
>     - Establecer métricas de progreso de aprendizaje

---

## 💡 Capturas Rápidas

> [!tip] 🧠 Inbox de Ideas **Ideas pendientes de procesar:**
> 
> - _[Agregar ideas aquí durante el día]_
> 
> **Próximo procesamiento:** _[Fecha]_

### 📝 Notas Rápidas del Día

> [!info] ✍️ Pensamientos y Observaciones _[Usar esta sección para capturar pensamientos rápidos que luego se procesarán en las notas correspondientes]_
> 
> ## **Hoy observé:**

---

## 🎨 Inspiración y Motivación

> [!quote] 💫 Frase del Día _"El éxito es la suma de pequeños esfuerzos repetidos día tras día."_ - Robert Collier

### 🌟 Logros Recientes

> [!success] 🏆 Celebrar los Wins
> 
> - [ ] Completé la estructura básica del vault de Obsidian
> - [ ] Documenté todos los métodos principales de estudio
> - [ ] Establecí sistema inicial de organización de espacios
> 
> **Último logro significativo:** _[Actualizar regularmente]_

---

## 🔄 Rutinas de Mantenimiento

### ⚡ Diariamente (5 min)

> [!tip] 📅 Mantenimiento Diario
> 
> - [ ] Actualizar progress de hábitos clave
> - [ ] Capturar 3 ideas/pensamientos importantes
> - [ ] Revisar objetivos del día
> - [ ] Procesar inbox de ideas si >5 items

### 📊 Semanalmente (30 min)

> [!info] 🗓️ Revisión Semanal
> 
> - [ ] Completar [[Dashboard Semanal]]
> - [ ] Revisar y actualizar objetivos semanales
> - [ ] Analizar métricas de la semana
> - [ ] Planificar próxima semana
> - [ ] Actualizar [[Tracking de Hábitos]]

### 🎯 Mensualmente (1 hora)

> [!warning] 📈 Revisión Mensual
> 
> - [ ] Evaluar progreso de [[Objetivos 2026]]
> - [ ] Revisar y actualizar sistema de notas
> - [ ] Identificar áreas de mejora
> - [ ] Planificar enfoque del próximo mes
> - [ ] Celebrar logros y aprendizajes

---

## 🛠️ Mantenimiento del Sistema

> [!info] ⚙️ Estado del Vault **Notas creadas:** 22 **Enlaces rotos:** 0 _(revisar semanalmente)_ **Última reorganización:** _[Fecha]_ **Próxima limpieza:** _[Fecha + 1 mes]_

### 🔧 Tareas de Mantenimiento Pendientes

- [x] Crear [[Dashboard Semanal]]
- [x] Crear [[Objetivos 2026]]
- [x] Crear [[Tracking de Hábitos]]
- [x] Revisar todos los enlaces internos
- [x] Actualizar tags de las notas existentes

---

## 📚 Recursos y Referencias

> [!quote] 🔗 Notas Relacionadas **Sistema Principal:**
> - [[Enlaces Rápidos]] Acceso directo a herramientas frecuentes
> - [[Análisis de Tiempo]] Seguimiento semanal del progreso anual
> - [[Hábitos de Estudio]] Planificación semanal académica 
> - [[Gestión del Tiempo]] Organización temporal semanal 
> - [[Objetivos 2026]] - Metas y seguimiento anual
> - [[Tracking de Hábitos]] - Monitoreo de comportamientos clave
> 
> **Áreas de Desarrollo:**
> 
> - [[Productividad Digital]] - Base del sistema de eficiencia
> - [[Gestión del Estrés]] - Fundamento del bienestar
> - [[Organización Física del Espacio]] - Optimización del entorno

---

**🔄 Última actualización:** `= date(now)` **⏰ Próxima revisión:** Todos los domingos a las 18:00

---

**Tags:** #dashboard #home #control-central #objetivos #habitos #productividad #bienestar #organizacion