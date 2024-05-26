from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Database connection details
    MYSQLHOST = "monorail.proxy.rlwy.net"
    MYSQLPASSWORD = "ywsSqojfvtsIjQUqILlvNAmnBbBsyDqB"
    MYSQLPORT = 47039
    MYSQLUSER = "root"
    MYSQL_DATABASE = "SCE"
    MYSQL_PRIVATE_URL = "mysql://root:ywsSqojfvtsIjQUqILlvNAmnBbBsyDqB@mysql.railway.internal:3306/railway"
    MYSQL_URL = "mysql://root:ywsSqojfvtsIjQUqILlvNAmnBbBsyDqB@monorail.proxy.rlwy.net:47039/railway"
    MYSQL_TABLE = "alumnos"

    # Connect to the database
    try:
        db = mysql.connector.connect(
            host=MYSQLHOST,
            user=MYSQLUSER,
            password=MYSQLPASSWORD,
            port=MYSQLPORT,
            database=MYSQL_DATABASE
        )
        print("Conexión a la base de datos exitosa")
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return "Error al conectar a la base de datos"

    # Create a cursor object
    cursor = db.cursor()

    # Get the search parameters from the URL
    cedula = request.args.get('cedula', '')
    apellido = request.args.get('apellido', '')

    # Construct the SQL query with filters
    query = "SELECT cedula, nombre, apellido1, apellido2, tel, email FROM alumnos"
    filters = []
    if cedula:
        filters.append(f"cedula LIKE '%{cedula}%'")
    if apellido:
        filters.append(f"apellido1 LIKE '%{apellido}%' OR apellido2 LIKE '%{apellido}%'")
    if filters:
        query += " WHERE " + " AND ".join(filters)

    # Execute the SQL query
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        print(f"Datos recuperados: {rows}")
    except mysql.connector.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return "Error al ejecutar la consulta"

    # Pass the data to the template
    return render_template('index2.html', data=rows)

    # Close the database connection
    db.close()

if __name__ == '__main__':
    app.run()