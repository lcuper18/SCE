import mysql.connector

def test():
    # Database connection details
    MYSQLHOST = "monorail.proxy.rlwy.net"
    MYSQLUSER = "root"
    MYSQLPASSWORD = "ywsSqojfvtsIjQUqILlvNAmnBbBsyDqB"
    MYSQLPORT = 47039
    MYSQL_DATABASE = "railway"

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
    