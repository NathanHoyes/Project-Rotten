from FoodObjects.Wastage import Wastage


# creates an admin object with the row results
def map_row(row_iterator: list) -> Wastage:
    row = next(row_iterator)
    return Wastage(row[0], row[1], row[2], row[3], row[4], row[5])


# creates a list of admin objects from the supplied query result
def map_multiple_rows(query_result: iter) -> list:
    wastage_result = []

    row = next(query_result)

    while True:
        try:
            wastage_result.append(Wastage(row[0], row[1], row[2], row[3], row[4], row[5]))
            row = next(query_result)
        except StopIteration:
            break

    return wastage_result
