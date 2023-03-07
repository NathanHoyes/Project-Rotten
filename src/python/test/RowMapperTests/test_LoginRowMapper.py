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

    def test_should_insert_value(self):
        self.setup_db()
        self.executor.insert_row("test_token_insert", "test_email_insert")
        result = self.executor.get_row_by_id(3)
        login = map_row(result)
        self.assertEqual(login.loginID, 3)
        self.assertEqual(login.loginTokenHash, "ac1c320ba378f55c2e246806ea91a4b7c78f2b875f135b6ab7a4c163bcab76e1")
        self.assertEqual(login.hashedEmail, "efb94aa4fd0ee88a727cc52515e4410a18f2f59bb5464e7c3114b6290b89a775")

    def setup_db(self):
        self.db.executeSqlScript("../../../resources/create_db_sql.sql")

