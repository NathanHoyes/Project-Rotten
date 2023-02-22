from DatabaseConnector.DatabaseConnector import DatabaseConnector


class AdminDatabaseExecutor():

    def __init__(self, database_connector : DatabaseConnector):
        self.database_connector = database_connector

    # This class will be used to interact with the Admin table