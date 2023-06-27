import pymysql

def connect_to_mysql():
    connection = pymysql.connect(host="localhost", port=3306, user="root", password="password", database="my_database")
    return connection

def disconnect_from_mysql(connection):
    connection.close()

if __name__ == "__main__":
    connection = connect_to_mysql()
    disconnect_from_mysql(connection)
