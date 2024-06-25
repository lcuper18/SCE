from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
config = {
    'host': 'monorail.proxy.rlwy.net',
    'user': 'root',
    'password': 'ywsSqojfvtsIjQUqILlvNAmnBbBsyDqB',
    'port': 47039,
    'database': 'SCE_Database'
}

def get_db_connection():
    return mysql.connector.connect(**config)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM login WHERE id_docente = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    if user:
        return redirect(url_for('dashboard'))
    else:
        return "Invalid credentials", 401

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/lista_personal')
def lista_personal():
    return render_template('lista_personal.html')

@app.route('/get_docentes', methods=['GET'])
def get_docentes():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
    SELECT id_docente, 
    nombre, 
    apellido1, 
    apellido2, 
    telefono, 
    email, 
    fecha_nacimiento, 
    direccion,
    TIMESTAMPDIFF(YEAR, fecha_nacimiento, CURDATE()) AS edad
    FROM Docentes
    """)
    docentes = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(docentes)

if __name__ == '__main__':
    app.run(debug=True)