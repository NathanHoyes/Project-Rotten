from LocationsObjects.LocationObject import Location


# Create a location object with query results
def map_row(row_iterator: list) -> Location:
    row = next(row_iterator)
    return Location(row[0], row[1])


def map_multiple_rows(query_results: iter) -> list:
    location_results = []

    for row in query_results:
        location_results.append(Location(row[0], row[1]))

    return location_results
