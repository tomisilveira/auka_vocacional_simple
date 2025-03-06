# Auka Vocacional


Auka Vocacional es una aplicación web interactiva que ayuda a los usuarios a descubrir su vocación profesional mediante un test divertido y amigable. El sistema utiliza la API de Gemini para generar preguntas personalizadas y sugerencias de áreas de estudio basadas en las respuestas del usuario. Los datos recolectados se guardan automáticamente en una hoja de cálculo de Google Sheets para su posterior análisis.

---

## Características Principales

- **Test Vocacional Interactivo**: 10 preguntas de opción múltiple generadas por Gemini.
- **Resultados Personalizados**: Sugerencias de áreas de estudio basadas en las respuestas del usuario.
- **Integración con Google Sheets**: Los datos se guardan automáticamente en una hoja de cálculo.
- **Diseño Responsive**: Interfaz amigable y adaptable a diferentes dispositivos.
- **Seguridad**: Uso de variables de entorno para proteger claves API y credenciales.

---

## Tecnologías Utilizadas

- **Frontend**: HTML, CSS, JavaScript.
- **Backend**: Python, Flask.
- **APIs**: Gemini API, Google Sheets API.
- **Herramientas**: Google Cloud, GitHub.

---

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

1. **Clona el Repositorio**:
   ```bash
   git clone https://github.com/tomisilveira/auka_vocacional_simple
   cd auka-vocacional

   Instala las Dependencias:

bash
Copy
pip install -r requirements.txt
Configura las Variables de Entorno:

Crea un archivo .env en la raíz del proyecto y agrega las siguientes variables:

plaintext
Copy
SECRET_KEY=tu_clave_secreta
GEMINI_API_KEY=tu_api_key_de_gemini
GOOGLE_CREDENTIALS_JSON='{...}'  # JSON de credenciales de Google
Asegúrate de que el JSON de credenciales esté correctamente escapado.

Configura Google Sheets:

Crea una hoja de cálculo en Google Sheets y compártela con el correo electrónico de la cuenta de servicio (client_email en el JSON de credenciales).

Nombra las columnas: Nombre, Correo Electrónico, Localidad, Edad, Preguntas, Respuestas, Resultados.

Ejecuta la Aplicación:

bash
Copy
python app.py
Accede a la Aplicación:

Abre tu navegador y visita http://127.0.0.1:5000.

Estructura del Proyecto
Copy
auka-vocacional/
│
├── app.py                  # Archivo principal de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Variables de entorno (clave secreta, API Key, credenciales de Google)
├── .gitignore              # Archivo para ignorar archivos sensibles
├── README.md               # Documentación del proyecto
├── static/                 # Carpeta para archivos estáticos (CSS, JS, imágenes)
│   └── styles.css          # Estilos CSS
├── templates/              # Carpeta para plantillas HTML
│   ├── index.html          # Página de inicio
│   ├── test.html           # Página del test
│   └── results.html        # Página de resultados
└── scripts.js              # Archivo JavaScript para transiciones


Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto, sigue estos pasos:

Haz un fork del repositorio.

Crea una rama para tu feature o corrección:

bash
Copy
git checkout -b nombre-de-tu-feature
Realiza tus cambios y haz commit:

bash
Copy
git commit -m "Agrega nueva funcionalidad"
Envía un pull request.

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

Nombre: Tomás Santiago Silveira

Email: [tsilveira@neuquen.gov.ar]

GitHub: tu-usuario

¡Gracias por usar Auka Vocacional! Esperamos que te sea útil para descubrir tu vocación profesional. 🚀