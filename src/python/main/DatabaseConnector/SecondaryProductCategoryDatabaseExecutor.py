from DatabaseConnector.DatabaseConnector import DatabaseConnector


class SecondaryProductCategoryDatabaseExecutor:
    select_by_id_sql = "SELECT * FROM secondaryproductcategory WHERE SecondaryProductCategoryID = %s"
    select_all_sql = "SELECT * FROM secondaryproductcategory"
    insert_sql = "INSERT INTO secondaryproductcategory (SecondaryProductCategoryName) VALUES(%s)"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id: int) -> iter:
        params = (id, )
        return self.database_connector.executeSelectStatement(self.select_by_id_sql, params)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql, None)

    def insert_row(self, category_name) -> None:
        params = (category_name, )
        self.database_connector.executeUpdateStatement(self.insert_sql, params)


