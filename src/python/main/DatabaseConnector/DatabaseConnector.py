import mysql.connector
from mysql.connector import Error

from dotenv import dotenv_values

class DatabaseConnector():

    def __init__(self):
        config = dotenv_values(".env")
        self.host = "localhost"
        self.database = "rotten_test_database"
        self.username = "root"
        self.password = "password"
        
        # TODO get the environment variables working - this doesn't currently work
        #self.host = config["HOST"]
        #self.database = config["DATABASE"]
        #self.username = config["USERNAME"]
        #self.password = config["PASSWORD"]


    # will return an iterator of tuples which represent the rows returned by the SQL statement
    def executeSelectStatement(self, sql : str, params : tuple) -> iter:
        # ensure this is a select statement
        if self.isSelectStatement(sql):
            return self.exectuteSql(sql, params)


    # will execute a statement to update the database i.e. NOT a SELECT statement
    def executeUpdateStatement(self, sql : str, params : tuple) -> None:
        # ensure this is an update statement
        if self.isUpdateStatement(sql):
            return self.exectuteSql(sql, params)

    
    # will execute multiple update statements in a loop inside a single database connection and the close the connection
    def executeMultipleUpdateStatements(self, sqlStatements : list) -> None:
        try:
            connection = mysql.connector.connect(host=self.host,
                                                database=self.database,
                                                user=self.username,
                                                password=self.password,
                                                autocommit = True)
            
            if connection.is_connected():
                cursor = connection.cursor(buffered=True)

                for statement in sqlStatements:
                    # ensure the statement is an update statement
                    if self.isUpdateStatement(statement):
                        cursor.execute(statement)

        except Error as e:
            raise Exception(e)

        # must always make sure connection is closed no matter what happens
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    # Function to execute a single sql statement in a single database connection and close the connection
    # Will return an iterator of values returned from sql statement
    def exectuteSql(self, sql : str, params : tuple) -> iter:
        
        result = None

        try:
            connection = mysql.connector.connect(host=self.host,
                                                database=self.database,
                                                user=self.username,
                                                password=self.password,
                                                autocommit = True)
            
            if connection.is_connected():
                cursor = connection.cursor(buffered=True)
                cursor.execute(sql, params=params)
                result = iter(cursor.fetchall())


        except Error as e:
            raise Exception(e)

        # must always make sure connection is closed no matter what happens
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
            
            return result     


    def executeSqlScript(self, filePath : str) -> None:
        try:
            connection = mysql.connector.connect(host=self.host,
                                                database=self.database,
                                                user=self.username,
                                                password=self.password,
                                                autocommit = True)
            
            cursor = connection.cursor()
            if connection.is_connected():
                with open(filePath, "r") as sql_file:
                    cursor.execute(sql_file.read(), multi=True)

        except Error as e:
            print(e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    # check if the statement is a select statement
    def isSelectStatement(self, sql : str) -> bool:
        return sql.upper().startswith("SELECT")


    # check if the statement is an update i.e. NOT a SELECT statement
    def isUpdateStatement(self, sql : str) -> bool:
        return not sql.upper().startswith("SELECT")

