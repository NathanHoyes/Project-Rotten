from DatabaseConnector.DatabaseConnector import DatabaseConnector


class ProductDatabaseConnector:
    select_by_id_sql = "SELECT * FROM products WHERE ProductID = %s"
    select_all_sql = "SELECT * FROM products"
    insert_sql = "INSERT INTO products " \
                "(ProductName, PrimaryProductCategoryID, SecondaryProductCategoryID, UnitCostPence, UnitWeightGrams) " \
                "VALUES (%s, %s, %s, %s, %s)"
    delete_sql = "DELETE FROM products WHERE ProductID = %s"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id: int) -> iter:
        params = (id, )
        return self.database_connector.executeSelectStatement(self.select_by_id_sql, params)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql, None)

    def insert_row(self, product_name : str, primary_category : int, secondary_category : int,
                   unit_cost : int, unit_weight : int) -> None:
        if self.validate_insert(unit_cost, unit_weight):
            params = (product_name, primary_category, secondary_category, unit_cost, unit_weight)
            self.database_connector.executeUpdateStatement(self.insert_sql, params)

    def delete_row(self, productID: int) -> None:
        params = (productID, )
        self.database_connector.executeUpdateStatement(self.delete_sql, params)

    def validate_insert(self, unit_cost : int, unit_weight : int) -> bool:
        return unit_cost > 0 and unit_weight > 0
