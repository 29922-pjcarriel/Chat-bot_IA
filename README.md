# Chat-bot_IA
# 🤖 Guía Completa de Instalación de RASA 2.8.27 en Windows

## 📘 Descripción

Rasa es una plataforma **open source** para crear asistentes virtuales y chatbots inteligentes basados en **procesamiento de lenguaje natural (NLP)**.  
Esta guía explica paso a paso cómo instalar **Rasa 2.8.27** en **Windows 10/11**, utilizando **Python 3.8**, que es la versión más estable y compatible con esta versión de Rasa.

---

## 🧩 Requisitos previos

Antes de comenzar la instalación, asegúrate de tener los siguientes componentes:

| Componente | Versión recomendada | Descripción |
|-------------|----------------------|--------------|
| **Python** | 3.8.x | Versión estable compatible con TensorFlow 2.6 |
| **Pip** | ≥ 21.0 | Administrador de paquetes de Python |
| **Microsoft Visual C++ Build Tools** | 2022 | Necesario para compilar librerías en C/C++ |
| **Windows** | 10 o 11 (64 bits) | Sistema operativo compatible |

---

## ⚙️ 1. Instalación de Python 3.8

1. Descarga el instalador de **Python 3.8.x** desde el sitio oficial:  
   👉 [https://www.python.org/downloads/release/python-380/](https://www.python.org/downloads/release/python-380/)

2. Durante la instalación:
   - ✅ Marca la opción **“Add Python to PATH”**
   - Haz clic en **“Customize installation”**
   - Asegúrate de marcar **pip**, **tcl/tk**, y **Add Python to environment variables**
   - Luego selecciona **Install Now**

3. Verifica la instalación ejecutando en PowerShell o CMD:

   ```bash
   python --version
   pip --version
