from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Palmitas1973',
    'port': 3306,
    'database': 'SCE'
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
    direccion
    FROM Docentes
    """)
    docentes = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(docentes)

@app.route('/get_docente/<id>', methods=['GET'])
def get_docente(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
    SELECT id_docente, 
    nombre, 
    apellido1, 
    apellido2, 
    telefono, 
    email, 
    direccion
    FROM Docentes
    WHERE id_docente = %s
    """, (id,))
    docente = cursor.fetchone()
    cursor.close()
    connection.close()
    return jsonify(docente)

@app.route('/update_docente/<id>', methods=['POST'])
def update_docente(id):
    data = request.form.to_dict()
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
    UPDATE Docentes
    SET nombre = %s, apellido1 = %s, apellido2 = %s, telefono = %s, email = %s, direccion = %s
    WHERE id_docente = %s
    """
    values = (data['nombre'], data['apellido1'], data['apellido2'], data['telefono'], data['email'], data['direccion'], id)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'success': True})

@app.route('/delete_docente/<id>', methods=['DELETE'])
def delete_docente(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Docentes WHERE id_docente = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)