from unittest import TestCase

from DatabaseConnector.AdminDatabaseExecutor import AdminDatabaseExecutor
from DatabaseConnector.DatabaseConnector import DatabaseConnector
from RowMappers.AdminRowMapper import *


class Test(TestCase):

    executor = AdminDatabaseExecutor()
    db = DatabaseConnector()

    def test_map_row(self):
        self.setup_db()
        result = self.executor.get_row_by_id(1)
        admin = map_row(result)
        self.assertEqual(admin.adminID, 1)
        self.assertEqual(admin.staffID, 1)


    def test_map_multiple_rows(self):
        self.setup_db()
        result = self.executor.get_all_rows()
        admin_list = map_multiple_rows(result)
        admin = admin_list[1]
        self.assertEqual(admin.adminID, 2)
        self.assertEqual(admin.staffID, 2)



    def setup_db(self):
        self.db.executeSqlScript("../../../resources/create_db_sql.sql")