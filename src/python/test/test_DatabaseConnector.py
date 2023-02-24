from unittest import TestCase

from DatabaseConnector.DatabaseConnector import DatabaseConnector
class TestDatabaseConnector(TestCase):
    def test_should_correctly_select_all_items_from_table(self, expected_size=3):
        self.setUp()
        db = DatabaseConnector()
        sql = "SELECT * FROM Staff"
        result = db.executeSelectStatement(sql)
        self.assertEqual(expected_size, len(list(result)),
                         f"Incorrect size of record: Expected record of size {expected_size} but was size {len(list(result))}")

    def test_should_correctly_select_by_id(self, expected_size=1):
        self.setUp()
        db = DatabaseConnector()
        sql = "SELECT * FROM Staff WHERE StaffID = 1"
        result = db.executeSelectStatement(sql)
        self.assertEqual(expected_size, len(list(result)),
                         f"Incorrect size of record: Expected record of size {expected_size} but was size {len(list(result))}")

    def test_should_correctly_update_single_row_by_id(self, expected_size=1):
        self.setUp()
        db = DatabaseConnector()
        sql = "UPDATE Staff SET FirstName = 'Testman' WHERE StaffID = 1"

        sql = "SELECT * FROM Staff WHERE FirstName = 'Testman'"
        result = db.executeSelectStatement(sql)

        self.assertEqual(expected_size, len(list(result)),
                         f"Incorrect size of record: Expected record of size {expected_size} but was size {len(list(result))}")

    def test_should_correctly_delete_single_row_by_id(self, expected_size=1):
        self.setUp()
        db = DatabaseConnector()
        sql = "DELETE * FROM Staff WHERE StaffID = 1"

        sql = "SELECT * FROM Staff WHERE StaffID = 1"
        result = db.executeSelectStatement(sql)
        self.assertEqual(expected_size, len(list(result)),
                         f"Incorrect size of record: Expected record of size {expected_size} but was size {len(list(result))}")

    def test_execute_select_statement_should_not_exectute_update_statement(self):
        self.setUp()
        db = DatabaseConnector()
        sql = "DELETE * FROM Staff WHERE StaffID = 1"
        result = db.executeUpdateStatement(sql)
        self.assertEqual(result, None,
                         f"Unexpected Value: Expected record of type None but was of type {type(result)}")

    def test_execute_update_statement_should_not_execute_select_statement(self):
        self.setUp()
        db = DatabaseConnector()
        sql = "SELECT * FROM Staff WHERE StaffID = 1"
        result = db.executeUpdateStatement(sql)
        self.assertEqual(result, None,
                         f"Unexpected Value: Expected record of type None but was of type {type(result)}")

    # resets the DB by executing the .sql file
    def setup(self):
        db = DatabaseConnector()
        db.executeSqlScript("E:\\Project Rotten\\Project-Rotten\\src\\resources\\create_db_sql.sql")
