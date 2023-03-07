from unittest import TestCase
from RowMappers.ProductRowMapper import *
from DatabaseConnector.ProductDatabaseExecutor import ProductDatabaseConnector
from DatabaseConnector.DatabaseConnector import DatabaseConnector

class Test(TestCase):

    executor = ProductDatabaseConnector()
    db = DatabaseConnector()

    def test_map_row(self):
        self.setup_db()
        result = self.executor.get_row_by_id(1)
        product = map_row(result)
        self.assertEqual(product.productID, 1)
        self.assertEqual(product.productName, "Chicken Breast")
        self.assertEqual(product.primaryProductCategory, 1)
        self.assertEqual(product.secondaryProductCategory, 2)
        self.assertEqual(product.unitCostPence, 500)
        self.assertEqual(product.unitWeightGrams, 220)


    def test_map_multiple_rows(self):
        self.setup_db()
        result = self.executor.get_all_rows()
        product_list = map_multiple_rows(result)
        product = product_list[1]
        self.assertEqual(product.productID, 2)
        self.assertEqual(product.productName, "Fillet Steak")
        self.assertEqual(product.primaryProductCategory, 1)
        self.assertEqual(product.secondaryProductCategory, 1)
        self.assertEqual(product.unitCostPence, 1200)
        self.assertEqual(product.unitWeightGrams, 280)


    def test_should_insert_value(self):
        self.setup_db()
        self.executor.insert_row("Test Product", 2, 3, 100, 100)
        result = self.executor.get_all_rows()
        product_list = map_multiple_rows(result)
        product = product_list[-1]
        self.assertEqual(product.productName, "Test Product")
        self.assertEqual(product.primaryProductCategory, 2)
        self.assertEqual(product.secondaryProductCategory, 3)
        self.assertEqual(product.unitCostPence, 100)
        self.assertEqual(product.unitWeightGrams, 100)

    def test_should_not_insert_value(self):
        self.setup_db()
        self.executor.insert_row("Test Product", 2, 3, -100, -100)
        result = self.executor.get_all_rows()
        product_list = map_multiple_rows(result)
        product = product_list[-1]
        self.assertNotEqual(product.productID, 12)

    def setup_db(self):
        self.db.executeSqlScript("../../../resources/create_db_sql.sql")