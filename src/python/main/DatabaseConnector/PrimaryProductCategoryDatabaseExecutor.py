from DatabaseConnector.DatabaseConnector import DatabaseConnector


class PrimaryProductCategoryDatabaseExecutor:

    select_by_id_sql = "SELECT * FROM primaryproductcategory WHERE PrimaryProductCategoryID = "
    select_all_sql = "SELECT * FROM primaryproductcategory"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id: int) -> iter:
        sql = self.select_by_id_sql + str(id)
        return self.database_connector.executeSelectStatement(sql)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql)
