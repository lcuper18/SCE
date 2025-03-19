import mysql.connector

def test():
    # Database connection details
    MYSQLHOST = "localhost"
    MYSQLUSER = "root"
    MYSQLPASSWORD = "Palmitas1973"
    MYSQLPORT = 3306
    MYSQL_DATABASE = "SCE"

    try:
        # Connect to the database
        db = mysql.connector.connect(
            host=MYSQLHOST,
            user=MYSQLUSER,
            password=MYSQLPASSWORD,
            port=MYSQLPORT,
            database=MYSQL_DATABASE
        )
        return("OK")
    except mysql.connector.Error as error:
        return("Error:", error)
    