from flask import Flask, render_template, request, redirect, url_for, session
import google.generativeai as genai
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Clave secreta desde .env

# Configura la API de Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # API Key de Gemini desde .env

# Crear una instancia del modelo
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Configura la API de Google Sheets
def setup_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        eval(os.getenv("GOOGLE_CREDENTIALS_JSON")), scope
    )
    client = gspread.authorize(creds)
    sheet = client.open("Auka_Vocacional_Data").sheet1  # Nombre de la hoja de cálculo
    return sheet

# Guardar datos en Google Sheets
def save_to_google_sheets(data):
    sheet = setup_google_sheets()
    sheet.append_row(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_test', methods=['POST'])
def start_test():
    # Obtener datos del formulario
    session['user_data'] = {
        'name': request.form['name'],
        'email': request.form['email'],
        'location': request.form['location'],
        'age': request.form['age']
    }
    session['questions'] = []  # Lista para almacenar preguntas
    session['responses'] = []  # Lista para almacenar respuestas
    session['current_question'] = 0  # Iniciar con la primera pregunta

    # Generar las preguntas con Gemini
    prompt = """
    Genera 10 preguntas divertidas y amigables (asarosas) para un test vocacional.
    Cada pregunta debe tener exactamente 3 opciones de respuesta, etiquetadas como a), b) y c).
    Formato:
    1. Pregunta 1
    a) Opción 1
    b) Opción 2
    c) Opción 3
    2. Pregunta 2
    a) Opción 1
    b) Opción 2
    c) Opción 3
    ...
    """
    try:
        response = model.generate_content(prompt)
        questions = response.text.strip().split('\n\n')  # Separar las preguntas
        session['questions'] = questions
    except Exception as e:
        return f"Error al generar preguntas: {e}", 500

    return redirect(url_for('test'))

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        # Guardar la respuesta del usuario
        response = request.form.get('response')
        session['responses'].append(response)
        session['current_question'] += 1  # Avanzar a la siguiente pregunta

    # Verificar si ya se respondieron todas las preguntas
    if session['current_question'] >= len(session['questions']):
        return redirect(url_for('results'))

    # Obtener la pregunta actual
    current_question = session['questions'][session['current_question']]
    question_lines = current_question.strip().split('\n')
    question = question_lines[0]  # La primera línea es la pregunta
    option_a = question_lines[1]  # La segunda línea es la opción a)
    option_b = question_lines[2]  # La tercera línea es la opción b)
    option_c = question_lines[3]  # La cuarta línea es la opción c)

    return render_template('test.html', question=question, option_a=option_a, option_b=option_b, option_c=option_c)

@app.route('/results')
def results():
    # Generar resultados con la API de Gemini
    prompt = f"""
    Basado en estas respuestas: {session['responses']}, sugiere 3 áreas de estudio que podrían ser adecuadas para el usuario.
    Las áreas de estudio deben ser amplias y relevantes para sus intereses y habilidades.
    Formato:
    1. Área de Estudio 1
    2. Área de Estudio 2
    3. Área de Estudio 3
    Explicación: [Breve explicación psicoanalítica de por qué estas áreas podrían ser una buena opción]
    """
    try:
        response = model.generate_content(prompt)
        results = response.text
    except Exception as e:
        return f"Error al generar resultados: {e}", 500

    # Guardar datos en Google Sheets
    user_data = session['user_data']
    data_to_save = [
        user_data['name'],
        user_data['email'],
        user_data['location'],
        user_data['age'],
        "\n".join(session['questions']),  # Preguntas
        "\n".join(session['responses']),  # Respuestas
        results  # Resultados
    ]
    save_to_google_sheets(data_to_save)

    return render_template('results.html', results=results, user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)