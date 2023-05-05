from unittest import TestCase

from DatabaseConnector.DatabaseConnector import DatabaseConnector
class TestDatabaseConnector(TestCase):

    db = DatabaseConnector()

    def test_should_correctly_select_all_items_from_table(self, expected_size=3):
        self.setup_db()
        db = DatabaseConnector()
        sql = "SELECT * FROM Staff"
        result = db.executeSelectStatement(sql, None)
        self.assertEqual(expected_size, len(list(result)),
                         f"Incorrect size of record: Expected record of size {expected_size} but was size {len(list(result))}")

    def test_should_correctly_select_by_id(self, expected_size=1):
        self.setup_db()
        db = DatabaseConnector()
        sql = "SELECT * FROM Staff WHERE StaffID = %s"
        params =  (1, )
        result = db.executeSelectStatement(sql, params)
        self.assertEqual(expected_size, len(list(result)),
                         f"Incorrect size of record: Expected record of size {expected_size} but was size {len(list(result))}")

    def test_should_correctly_update_single_row_by_id(self, expected_size=1):
        self.setup_db()
        db = DatabaseConnector()
        update_sql = "UPDATE Staff SET FirstName = %s WHERE StaffID = %s"
        params = ("Testman", 1)
        db.executeUpdateStatement(update_sql, params)

        select_sql = "SELECT * FROM Staff WHERE FirstName = %s"
        search_params = ("Testman", )
        result = db.executeSelectStatement(select_sql, search_params)

        self.assertEqual(expected_size, len(list(result)),
                         f"Incorrect size of record: Expected record of size {expected_size} but was size {len(list(result))}")

    def test_should_correctly_delete_single_row_by_id(self, expected_size=1):
        self.setup_db()
        db = DatabaseConnector()
        delete_sql = "DELETE * FROM Staff WHERE StaffID = %s"
        params = (1, )
        db.executeUpdateStatement(delete_sql, params)

        sql = "SELECT * FROM Staff WHERE StaffID = %s"
        result = db.executeSelectStatement(sql, params)
        self.assertEqual(expected_size, len(list(result)),
                         f"Incorrect size of record: Expected record of size {expected_size} but was size {len(list(result))}")

    def test_execute_select_statement_should_not_exectute_update_statement(self):
        self.setup_db()
        db = DatabaseConnector()
        sql = "DELETE * FROM Staff WHERE StaffID = %s"
        params = (1, )
        result = db.executeUpdateStatement(sql, params)
        self.assertEqual(result, None,
                         f"Unexpected Value: Expected record of type None but was of type {type(result)}")

    def test_execute_update_statement_should_not_execute_select_statement(self):
        self.setup_db()
        db = DatabaseConnector()
        sql = "SELECT * FROM Staff WHERE StaffID = %s"
        params = (1, )
        result = db.executeUpdateStatement(sql, params)
        self.assertEqual(result, None,
                         f"Unexpected Value: Expected record of type None but was of type {type(result)}")

    # resets the DB by executing the .sql file
    def setup_db(self):
        self.db.executeSqlScript("../../../resources/create_db_sql.sql")
