#import mysql connector
import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "Dhanraj@22102001",
        database = "Edata"
    )

def insert_data():
    # create a query
    connection=get_connection()
    uid = int(input("Enter uid : "))
    name = input("Enter name : ")
    department = (input("Enter department : "))
    email = (input("Enter email : "))
    salary = int(input("Enter salary :"))
    date = input("Enter date : ")

    query  = f"insert into Edata values({uid}, '{name}', '{department}','{email}', '{salary}', '{date}');"  #query is nothing but string 

    # create a cursor to execute the query    #cursor is like of file pointer to execute a query we requred cursor
    cursor = connection.cursor()  

    # execute query using cursor
    cursor.execute(query) 

    # after execution of query commit your changes
    connection.commit()

    # close the cursor
    cursor.close()

    #close the connection with mysql server 
    connection.close()

    print("query has added")


insert_data()