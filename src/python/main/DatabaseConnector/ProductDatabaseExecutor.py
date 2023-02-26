from ..DatabaseConnector.DatabaseConnector import DatabaseConnector


class ProductDatabaseConnector:
    select_by_id_sql = "SELECT * FROM products WHERE ProductID = "
    select_all_sql = "SELECT * FROM products"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id: int) -> iter:
        sql = self.select_by_id_sql + str(id)
        return self.database_connector.executeSelectStatement(sql)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql)


    def insert_row(self, product_name : str, primary_category : int, secondary_category : int, unit_cost : int, unit_weight : int) -> None:
        insert_sql = f"INSERT INTO products " \
                     f"(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams)" \
                     f"VALUES ({product_name}, {primary_category}, {secondary_category}, {unit_cost}, {unit_weight})"
        self.database_connector.executeUpdateStatement(insert_sql)

    def delete_row(self, productID: int) -> None:
        delete_sql = f"DELETE FROM products WHERE ProductID = {productID}"
        self.database_connector.executeUpdateStatement(delete_sql)