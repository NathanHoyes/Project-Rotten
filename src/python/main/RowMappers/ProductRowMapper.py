from FoodObjects.Product import Product


# creates an admin object with the row results
def map_row(row_iterator: list) -> Product:
    row = next(row_iterator)
    return Product(row[0], row[1], row[2], row[3], row[4], row[5])


# creates a list of admin objects from the supplied query result
def map_multiple_rows(query_result: iter) -> list:
    product_result = []

    row = next(query_result)

    while True:
        try:
            product_result.append(Product(row[0], row[1], row[2], row[3], row[4], row[5]))
            row = next(query_result)
        except StopIteration:
            break

    return product_result