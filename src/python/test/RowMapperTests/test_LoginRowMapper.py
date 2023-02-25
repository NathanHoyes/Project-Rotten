from unittest import TestCase
from RowMappers.LoginRowMapper import *
from DatabaseConnector.LoginDatabaseExecutor import LoginDatabaseExecutor
from DatabaseConnector.DatabaseConnector import DatabaseConnector

class test_LoginRowMapper(TestCase):

    executor = LoginDatabaseExecutor()
    db = DatabaseConnector()
    def test_map_row(self):
        self.setup_db()
        result = self.executor.get_row_by_id(1)
        login = map_row(result)
        self.assertEqual(login.loginID, 1)
        self.assertEqual(login.loginTokenHash, "testHash")
        self.assertEqual(login.hashedEmail, "testEmail")


    def test_map_multiple_rows(self):
        self.setup_db()
        result = self.executor.get_all_rows()
        logins = map_multiple_rows(result)
        a_login = logins[1]
        self.assertEqual(a_login.loginID, 2)
        self.assertEqual(a_login.loginTokenHash, "f359e5ce5ee865e2448c07b69906c99bd3ae0fea22968088174a7eda5ba1dfaa")
        self.assertEqual(a_login.hashedEmail, "fdd8157ddd7d2ade12a3799aa9998a8de76d291c1f3ddce3b3bb7edb2f42c7a8")

    def setup_db(self):
        self.db.executeSqlScript("E:\\Project Rotten\\Project-Rotten\\src\\resources\\create_db_sql.sql")