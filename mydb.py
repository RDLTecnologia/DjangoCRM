import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Eh-Tricolor1'
)

cursorObject = dataBase.cursor()

try:
    cursorObject.execute("CREATE DATABASE RDLCRM")
    print("Banco de Dados Criado com Sucesso")
except ValueError as valueError:
    print(f"Problema com a criação do banco de dados valueError: {valueError}")
except Exception as ex:
    print(f"Problema com a criação do banco de dados Exception: {ex}")    

 