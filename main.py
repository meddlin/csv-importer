import csv

def make_sql_create(table_name: str, col_type_data):
    # what is needed for this method?
    # col_data = [
    #     {
    #         c1: varchar,
    #         c2: decimal,
    #     }
    # ]

    last_key = list(col_type_data.keys())[-1]
    query = f"create table {table_name} ("

    for key in col_type_data:
        if key == last_key:
            query = query + f"{key} {col_type_data[key]}"
        else:
            query = query + f"{key} {col_type_data[key]}, "

    query = query + ")"
    return query

def get_type(data):
    """
        Detect appropriate database type for Python type. The Python type 
        is based on the 
    """

    if isinstance(data, str):
        return "varchar"
    if isinstance(data, int):
        return "decimal"

def create_type_dictionary(row_dict):
    types = {}

    for key in row_dict:
        db_type = get_type(row_dict[key])

        clean_key = key.replace('"', '') # In case keys (file headers) are wrapped in quotes
        types[clean_key] = db_type
    
    return types

def create_table_name(filename: str):
    """Defaults to table name being the filename, without the extension."""

    if '.csv' in filename:
        return filename[:len(filename)-4]
    else:
        return filename

def main():
    filename = 'airtravel.csv'

    table_name = ''
    if '.csv' in filename:
        table_name = filename[:len(filename)-4]

    with open(filename, 'r', encoding = 'utf-8') as file:
        reader = csv.DictReader(file)

        # headers = reader.fieldnames
        # print(headers)
        row1 = next(reader)
        type_data = create_type_dictionary(row1)
        print(type_data)
        print( make_sql_create(table_name, type_data) )


if __name__ == "__main__":
    main()