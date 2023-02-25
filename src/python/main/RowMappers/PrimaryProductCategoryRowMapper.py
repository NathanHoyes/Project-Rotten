from CategoryObjects.PrimaryProductCategory import PrimaryProductCategory

# creates an admin object with the row results
def map_row(row_iterator: list) -> PrimaryProductCategory:
    row = next(row_iterator)
    return PrimaryProductCategory(row[0], row[1])


# creates a list of admin objects from the supplied query result
def map_multiple_rows(query_result: iter) -> list:
    category_result = []

    row = next(query_result)

    while True:
        try:
            category_result.append(PrimaryProductCategory(row[0], row[1]))
            row = next(query_result)
        except StopIteration:
            break

    return category_result
