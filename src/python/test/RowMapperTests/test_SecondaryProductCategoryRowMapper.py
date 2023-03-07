from unittest import TestCase
from RowMappers.SecondaryProductCategoryRowMapper import *
from DatabaseConnector.SecondaryProductCategoryDatabaseExecutor import SecondaryProductCategoryDatabaseExecutor
from DatabaseConnector.DatabaseConnector import DatabaseConnector


class Test(TestCase):

    executor = SecondaryProductCategoryDatabaseExecutor()
    db = DatabaseConnector()

    def test_map_row(self):
        self.setup_db()
        result = self.executor.get_row_by_id(1)
        product_category = map_row(result)
        self.assertEqual(product_category.secondaryProductCategoryId, 1)
        self.assertEqual(product_category.secondaryProductCategoryName, "Red Meat")

    def test_map_multiple_rows(self):
        self.setup_db()
        result = self.executor.get_all_rows()
        product_category_list = map_multiple_rows(result)
        product_category = product_category_list[1]
        self.assertEqual(product_category.secondaryProductCategoryId, 2)
        self.assertEqual(product_category.secondaryProductCategoryName, "White Meat")

    def test_should_insert_row(self):
        self.setup_db()
        self.executor.insert_row("Test Category")
        result = self.executor.get_all_rows()
        product_category_list = map_multiple_rows(result)
        product_category = product_category_list[-1]
        self.assertEqual(product_category.secondaryProductCategoryName, "Test Category")

    def setup_db(self):
        self.db.executeSqlScript("../../../resources/create_db_sql.sql")
