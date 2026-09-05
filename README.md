# Proyecto de Práctica Git, GitHub y PowerShell

Este repositorio fue desarrollado como parte de una práctica de **Git y GitHub utilizando PowerShell y Visual Studio Code**.

El objetivo del proyecto es aplicar los principales conceptos de control de versiones, incluyendo la creación de repositorios, commits, ramas, conexión con GitHub, operaciones remotas, resolución de conflictos y desarrollo de un pequeño proyecto web con HTML y CSS.

---

## 📌 Objetivo del proyecto

Aprender y aplicar de manera práctica el funcionamiento de **Git y GitHub**, comprendiendo la diferencia entre un repositorio local y uno remoto y utilizando correctamente los principales comandos de Git.

Durante el desarrollo del proyecto se trabajaron los siguientes conceptos:

- Repositorios locales y remotos.
- Commits.
- Ramas (branches).
- Área de preparación (staging area).
- Archivo `.gitignore`.
- Conexión con GitHub.
- Push y pull.
- Merge de ramas.
- Resolución de conflictos.
- Historial de cambios.
- Trabajo con HTML y CSS.
- Uso de PowerShell y Visual Studio Code.

---

## 🛠️ Tecnologías y herramientas utilizadas

- Git
- GitHub
- PowerShell
- Visual Studio Code
- HTML
- CSS
- Java
- Python

---

## 📁 Estructura del proyecto

El repositorio contiene los siguientes archivos principales:

```text
proyecto-git/
│
├── .gitignore
├── README.md
├── index.html
├── styles.css
├── Ejemplo.java
└── Ejemplo.py
```

### Descripción de los archivos

**README.md**  
Contiene la documentación general del proyecto y el proceso realizado durante la práctica.

**.gitignore**  
Permite indicar los archivos o directorios que Git no debe incluir en el seguimiento del repositorio.

**index.html**  
Contiene la estructura principal del pequeño proyecto web desarrollado durante la práctica.

**styles.css**  
Contiene los estilos utilizados para modificar la apariencia de la página web.

**Ejemplo.java**  
Archivo utilizado para practicar modificaciones, commits y nuevas características utilizando Java.

**Ejemplo.py**  
Archivo de ejemplo en Python incluido dentro del repositorio.

---

# 🚀 Proceso realizado

## 1. Configuración inicial de Git

Primero se verificó que Git estuviera instalado correctamente:

```powershell
git --version
```

Posteriormente se configuraron los datos del usuario:

```powershell
git config user.name "Nombre Apellido"
git config user.email "correo@ejemplo.com"
```

La configuración se puede verificar utilizando:

```powershell
git config --list
```

---

## 2. Creación del repositorio local

Se trabajó con un repositorio local para administrar los archivos del proyecto mediante Git.

Para inicializar un repositorio se utiliza:

```powershell
git init
```

Durante el proyecto se utilizaron diferentes archivos para realizar pruebas con Git.

---

## 3. Estado del repositorio

Para revisar constantemente los cambios realizados en los archivos se utilizó:

```powershell
git status
```

Este comando permite identificar:

- Archivos nuevos.
- Archivos modificados.
- Archivos preparados para un commit.
- Estado actual de la rama.

---

## 4. Área de preparación y commits

Los archivos modificados se agregaron al área de preparación utilizando:

```powershell
git add .
```

También se pueden agregar archivos individualmente:

```powershell
git add README.md
```

Después se registraron los cambios mediante commits:

```powershell
git commit -m "Mensaje descriptivo del cambio"
```

Los mensajes de los commits fueron utilizados para describir claramente las modificaciones realizadas en el proyecto.

---

## 5. Historial de commits

Para revisar el historial completo del repositorio se utilizó:

```powershell
git log
```

También se utilizó una versión resumida:

```powershell
git log --oneline
```

Esto permite observar de manera sencilla los commits realizados durante el desarrollo del proyecto.

---

## 6. Uso de .gitignore

Se creó un archivo:

```text
.gitignore
```

Su función es evitar que determinados archivos o carpetas sean incluidos en el seguimiento de Git.

Ejemplos de elementos que pueden ser ignorados:

```text
node_modules/
.env
*.log
.DS_Store
.vscode/
```

Después de configurar el archivo se verificó su funcionamiento mediante:

```powershell
git status
```

---

## 7. Conexión con GitHub

El repositorio local fue conectado con un repositorio remoto alojado en GitHub.

Para verificar la conexión remota se utilizó:

```powershell
git remote -v
```

El repositorio remoto se identifica mediante el nombre:

```text
origin
```

---

## 8. Operaciones remotas

Para subir los cambios desde el repositorio local hacia GitHub se utilizó:

```powershell
git push origin main
```

También se utilizó:

```powershell
git push
```

Para descargar e integrar cambios desde el repositorio remoto se utilizó:

```powershell
git pull
```

De esta manera se mantuvo sincronizado el repositorio local con GitHub.

---

# 🌿 Trabajo con ramas

Una parte importante de la práctica fue aprender a utilizar ramas para desarrollar cambios sin modificar directamente la rama principal.

La rama principal utilizada fue:

```text
main
```

Se crearon ramas adicionales para desarrollar nuevas características.

Por ejemplo:

```powershell
git checkout -b nueva-caracteristica
```

También se trabajó con la rama:

```text
equipo-web
```

Esta rama fue utilizada para desarrollar el proyecto web antes de integrarlo a `main`.

---

## 🔀 Fusión de ramas

Después de terminar los cambios realizados en una rama, se regresó a la rama principal:

```powershell
git checkout main
```

Posteriormente se realizó la fusión:

```powershell
git merge nombre-rama
```

Por ejemplo:

```powershell
git merge equipo-web
```

Esto permitió integrar el proyecto web desarrollado en una rama separada dentro de la rama principal.

---

# ⚠️ Resolución de conflictos

Durante la práctica se realizó una demostración real de un **conflicto de fusión**.

Se realizaron modificaciones diferentes sobre la misma parte del archivo `README.md` desde dos ramas distintas.

Al intentar fusionarlas, Git detectó el conflicto.

Git utiliza marcadores similares a los siguientes para indicar las diferencias:

```text
<<<<<<< HEAD
Cambio realizado en main
=======
Cambio realizado en otra rama
>>>>>>> nombre-rama
```

El conflicto fue solucionado manualmente seleccionando el contenido definitivo del archivo.

Después de resolverlo se ejecutó:

```powershell
git add README.md
```

Y posteriormente:

```powershell
git commit -m "merge: resolver conflicto en README"
```

De esta manera el conflicto quedó solucionado y la fusión pudo completarse correctamente.

---

# 💻 Proyecto práctico HTML y CSS

Como parte final de la práctica se desarrolló una pequeña página web utilizando:

- HTML
- CSS

El archivo:

```text
index.html
```

contiene la estructura de la página.

El archivo:

```text
styles.css
```

contiene su diseño y presentación visual.

El proyecto web fue desarrollado inicialmente dentro de una rama independiente:

```text
equipo-web
```

La rama fue creada utilizando:

```powershell
git checkout -b equipo-web
```

Los archivos fueron agregados al área de preparación:

```powershell
git add index.html styles.css
```

Posteriormente se realizó el commit:

```powershell
git commit -m "feat: agregar proyecto web HTML y CSS"
```

La rama fue subida a GitHub:

```powershell
git push -u origin equipo-web
```

Después se regresó a `main`:

```powershell
git checkout main
```

Y finalmente se integró el proyecto:

```powershell
git merge equipo-web
```

Los cambios de la rama principal fueron enviados a GitHub:

```powershell
git push origin main
```

---

# ☕ Práctica con Java

También se utilizó el archivo `Ejemplo.java` para practicar modificaciones y nuevas características.

Entre las pruebas realizadas se incluyeron:

- Impresión de mensajes en consola.
- Uso de ciclos.
- Variables.
- Condicionales.
- Incorporación de nuevas características.

Estos cambios permitieron practicar el flujo:

```text
Modificar archivo
      ↓
git status
      ↓
git add
      ↓
git commit
      ↓
git push
```

---

# 🔄 Flujo de trabajo utilizado

El flujo general utilizado durante el proyecto fue:

```text
Crear o modificar archivos
        ↓
git status
        ↓
git add
        ↓
git commit
        ↓
git push
        ↓
GitHub
```

Para trabajar con nuevas características:

```text
main
  ↓
Crear nueva rama
  ↓
Realizar modificaciones
  ↓
Commit
  ↓
Push de la rama
  ↓
Volver a main
  ↓
Merge
  ↓
Push a GitHub
```

---

# 🔐 Autenticación con GitHub

Durante la práctica también se revisó el uso de **Personal Access Tokens (PAT)** como mecanismo de autenticación con GitHub.

La configuración de almacenamiento de credenciales puede realizarse mediante:

```powershell
git config credential.helper store
```

El token permite autenticar determinadas operaciones realizadas entre Git y GitHub.

---

# 🔍 Comandos principales utilizados

| Comando | Función |
|---|---|
| `git --version` | Verificar la instalación de Git |
| `git config --list` | Consultar la configuración |
| `git init` | Inicializar un repositorio |
| `git status` | Consultar el estado del repositorio |
| `git add .` | Preparar todos los cambios |
| `git add archivo` | Preparar un archivo específico |
| `git commit -m "mensaje"` | Registrar cambios |
| `git log` | Consultar el historial |
| `git log --oneline` | Consultar el historial resumido |
| `git remote -v` | Verificar repositorios remotos |
| `git push` | Subir cambios al repositorio remoto |
| `git pull` | Descargar e integrar cambios remotos |
| `git branch` | Consultar o crear ramas |
| `git checkout rama` | Cambiar de rama |
| `git checkout -b rama` | Crear y cambiar a una nueva rama |
| `git merge rama` | Fusionar una rama |
| `git branch -d rama` | Eliminar una rama local |

---

# 🧩 Problemas y soluciones

Durante la práctica se revisaron algunos problemas comunes que pueden presentarse al utilizar Git.

### Conflictos de fusión

Cuando dos ramas modifican la misma parte de un archivo, Git puede generar un conflicto.

**Solución:** revisar manualmente el archivo, seleccionar el contenido correcto, agregarlo nuevamente con `git add` y realizar un commit.

### Cambios pendientes

Si Git indica que existen archivos modificados, se puede revisar la situación utilizando:

```powershell
git status
```

### Verificación del repositorio remoto

Para comprobar que el repositorio local está conectado correctamente con GitHub:

```powershell
git remote -v
```

---

# ✅ Resultado final

Al finalizar la práctica se logró:

- Configurar Git correctamente.
- Trabajar con un repositorio local.
- Crear y registrar commits.
- Utilizar `.gitignore`.
- Conectar Git con GitHub.
- Subir cambios al repositorio remoto.
- Descargar cambios mediante `git pull`.
- Crear y administrar ramas.
- Fusionar ramas.
- Resolver conflictos de fusión.
- Consultar el historial de commits.
- Desarrollar un pequeño proyecto con HTML y CSS.
- Trabajar con archivos Java y Python.
- Simular un flujo de trabajo colaborativo.
- Mantener sincronizadas las ramas locales y remotas.

---

# 🎯 Conclusión

Esta práctica permitió comprender el funcionamiento básico de **Git y GitHub** como herramientas para el control de versiones y el trabajo colaborativo.

El uso de ramas permitió desarrollar cambios de manera independiente antes de incorporarlos a la rama principal, mientras que la resolución de conflictos permitió comprender cómo actuar cuando diferentes versiones de un archivo presentan modificaciones incompatibles.

Finalmente, el proyecto HTML y CSS permitió aplicar estos conocimientos dentro de un ejercicio práctico, utilizando **PowerShell, Visual Studio Code, Git y GitHub** durante todo el proceso.

---

## 👤 Autor

**Andres Felipe Quintero Triviño**

Proyecto desarrollado como práctica de **Git, GitHub y PowerShell**.