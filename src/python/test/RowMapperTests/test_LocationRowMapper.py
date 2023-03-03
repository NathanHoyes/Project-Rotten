from unittest import TestCase
from RowMappers.LocationRowMapper import *
from DatabaseConnector.LocationDatabaseExecutor import LocationDatabaseConnector
from DatabaseConnector.DatabaseConnector import DatabaseConnector


class Test(TestCase):

    executor = LocationDatabaseConnector()
    db = DatabaseConnector()

    def test_map_row(self):
        self.setup_db()
        result = self.executor.get_row_by_id(1)
        location = map_row(result)
        self.assertEqual(location.locationID, 1)
        self.assertEqual(location.locationName, "The Frog and Dog")

    def test_map_multiple_rows(self):
        self.setup_db()
        results = self.executor.get_all_rows()
        locations = map_multiple_rows(results)
        self.assertEqual(locations[0].locationID, 1)
        self.assertEqual(locations[0].locationName, "The Frog and Dog")
        self.assertEqual(locations[1].locationID, 2)
        self.assertEqual(locations[1].locationName, "The Cat and Bat")
        self.assertEqual(locations[2].locationID, 3)
        self.assertEqual(locations[2].locationName, "The Pig and Fig")
        self.assertEqual(locations[3].locationID, 4)
        self.assertEqual(locations[3].locationName, "Testaraunt")

    def setup_db(self):
        self.db.executeSqlScript("../../../../resources/create_db_sql.sql")