import mysql.connector

# Database connection details
MYSQLHOST = "monorail.proxy.rlwy.net"
MYSQLPASSWORD = "ywsSqojfvtsIjQUqILlvNAmnBbBsyDqB"
MYSQLPORT = 47039
MYSQLUSER = "root"
MYSQL_DATABASE = "railway"
MYSQL_PRIVATE_URL = "mysql://root:ywsSqojfvtsIjQUqILlvNAmnBbBsyDqB@mysql.railway.internal:3306/railway"
MYSQL_URL = "mysql://root:ywsSqojfvtsIjQUqILlvNAmnBbBsyDqB@monorail.proxy.rlwy.net:47039/railway"
MYSQL_TABLE = "alumnos"

try:
    # Connect to the database
    db = mysql.connector.connect(
        host=MYSQLHOST,
        user=MYSQLUSER,
        password=MYSQLPASSWORD,
        port=MYSQLPORT,
        database=MYSQL_DATABASE
    )
    print("OK")
except mysql.connector.Error as error:
    print("Error:", error)