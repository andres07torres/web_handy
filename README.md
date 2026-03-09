# 🤟 Handy - Traductor de Lengua de Señas en Tiempo Real

![En Desarrollo](https://img.shields.io/badge/Estado-En%20Desarrollo-orange?style=for-the-badge)

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Django](https://img.shields.io/badge/Django-5.2.9-green)
![OpenCV](https://img.shields.io/badge/OpenCV-4.12-red)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Handy** es una aplicación web que utiliza inteligencia artificial y visión por computadora para traducir la lengua de señas a texto en tiempo real, rompiendo barreras de comunicación entre personas con discapacidad auditiva y oyentes.

## 📋 Descripción

Handy es un traductor de lengua de señas que funciona directamente desde el navegador web, utilizando la cámara del dispositivo para detectar y reconocer gestos de las manos. El sistema procesa los movimientos en tiempo real y los convierte en texto, facilitando la comunicación sin necesidad de equipos especializados o costosos.

### ✨ Características Principales

- 🎥 **Reconocimiento en Tiempo Real**: Traducción instantánea de señas a texto
- 🔒 **Privacidad Garantizada**: Todo el procesamiento ocurre en el navegador, sin enviar datos a servidores externos
- 📱 **Multiplataforma**: Funciona en computadoras, tablets y smartphones con cámara
- 🎨 **Interfaz Intuitiva**: Diseño moderno y fácil de usar con Bootstrap 5
- 📚 **Galería de Aprendizaje**: Diccionario visual de señas para aprender
- 🔍 **Búsqueda Inteligente**: Sistema de búsqueda en vivo con sugerencias
- 🌐 **Accesible**: No requiere instalación, funciona desde cualquier navegador moderno

## 🚀 Tecnologías Utilizadas

### Backend
- **Django 5.2.9** - Framework web de Python
- **Python 3.14** - Lenguaje de programación principal
- **OpenCV 4.12** - Procesamiento de imágenes y visión por computadora
- **Pillow 12.1** - Manipulación de imágenes
- **Gunicorn** - Servidor WSGI para producción
- **PostgreSQL** (psycopg2) - Base de datos
- **WhiteNoise** - Servir archivos estáticos

### Frontend
- **Bootstrap 5.3.8** - Framework CSS
- **Bootstrap Icons** - Iconografía
- **JavaScript (Vanilla)** - Interactividad del cliente
- **SweetAlert2** - Alertas y notificaciones elegantes
- **HTML5 & CSS3** - Estructura y estilos

### Inteligencia Artificial
- **OpenCV Contrib** - Módulos adicionales de visión artificial
- **MediaPipe** (implícito) - Detección de puntos clave de las manos

## 📦 Instalación

### Prerrequisitos
- Python 3.14 o superior
- pip (gestor de paquetes de Python)
- Node.js y npm (para dependencias de frontend)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/handy.git
cd handy
```

2. **Crear y activar entorno virtual**
```bash
# Windows
python -m venv env
env\Scripts\activate

# Linux/Mac
python3 -m venv env
source env/bin/activate
```

3. **Instalar dependencias de Python**
```bash
cd wwwRecon/proyecto
pip install -r requirements.txt
```

4. **Instalar dependencias de Node.js**
```bash
npm install
```

5. **Configurar la base de datos**
```bash
python manage.py migrate
```

6. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

7. **Ejecutar el servidor de desarrollo**
```bash
python manage.py runserver
```

8. **Acceder a la aplicación**
```
http://localhost:8000
```

## 🎯 Uso

1. **Iniciar la Cámara**: Haz clic en el botón "Iniciar" y permite el acceso a la cámara
2. **Posicionarse**: Colócate frente a la cámara con buena iluminación
3. **Realizar Señas**: Ejecuta los gestos del alfabeto o palabras en lengua de señas
4. **Ver Traducción**: El texto traducido aparecerá en tiempo real en el panel derecho
5. **Copiar o Limpiar**: Usa los botones para copiar el texto o limpiar la pantalla

### Recomendaciones para Mejores Resultados
- ✅ Asegúrate de tener buena iluminación
- ✅ Mantén las manos dentro del encuadre de la cámara
- ✅ Realiza los gestos de forma clara y pausada
- ✅ Evita fondos con mucho movimiento

## 📁 Estructura del Proyecto

```
proyecto-u/
├── env/                          # Entorno virtual de Python
└── wwwRecon/
    └── proyecto/
        ├── App/                  # Aplicación principal de Django
        │   ├── migrations/       # Migraciones de base de datos
        │   ├── static/           # Archivos estáticos
        │   │   ├── css/          # Estilos personalizados
        │   │   ├── img/          # Imágenes
        │   │   └── js/           # Scripts JavaScript
        │   ├── templates/        # Plantillas HTML
        │   │   ├── index.html
        │   │   ├── reconocimiento.html
        │   │   ├── funcionamiento.html
        │   │   └── galeria.html
        │   ├── models.py         # Modelos de datos
        │   ├── views.py          # Vistas y lógica
        │   └── admin.py          # Configuración del admin
        ├── proyecto/             # Configuración de Django
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── db.sqlite3            # Base de datos SQLite
        ├── manage.py             # Script de gestión de Django
        ├── requirements.txt      # Dependencias de Python
        └── package.json          # Dependencias de Node.js
```

## 🌟 Funcionalidades

### 1. Traductor en Tiempo Real
- Captura de video desde la cámara web
- Detección de 21 puntos clave en cada mano
- Procesamiento y reconocimiento de gestos
- Traducción instantánea a texto

### 2. Galería de Aprendizaje
- Diccionario visual de señas
- Imágenes de referencia del alfabeto
- Sistema de filtrado y búsqueda

### 3. Guía de Funcionamiento
- Explicación paso a paso del uso
- Historia del proyecto
- Información sobre la tecnología utilizada

### 4. Búsqueda Inteligente
- Búsqueda en vivo con sugerencias
- Resultados visuales con tarjetas
- Navegación rápida entre secciones

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar Handy:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 🐛 Reportar Problemas

Si encuentras algún bug o tienes sugerencias, por favor abre un [issue](https://github.com/andres07torres/wwwRecon) en GitHub.

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Carlos Andrés Torres** - *Desarrollo Inicial* - [Tu GitHub](https://github.com/andres07torres)

## 🙏 Agradecimientos

- A la comunidad de personas con discapacidad auditiva que inspiró este proyecto
- A los desarrolladores de OpenCV y Django por sus increíbles herramientas
- A todos los que contribuyen a hacer la tecnología más inclusiva

## 📞 Contacto

¿Preguntas o sugerencias? No dudes en contactar:

- 📧 Email: andres07torresg@gmail.com
- 💼 LinkedIn: [Tu Perfil](www.linkedin.com/in/carlos-torres-guaman)

---

⭐ Si este proyecto te ha sido útil, considera darle una estrella en GitHub

**Handy** - Rompiendo barreras lingüísticas con visión artificial e inteligencia artificial 🤟
