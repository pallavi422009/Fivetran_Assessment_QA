def create_table(cur, table_name: str, columns: dict, constraints: list = None):
    """
    Method to create table in database
    :param cur:psycopg2 Cursor object
    :param constraints: Optional. A list of constraints (e.g., PRIMARY KEY, FOREIGN KEY).
    :param columns: (dict): A dictionary where keys are column names and values are column data types.
    :param table_name: Name of the table to be created
    :return:

        Example:
    columns = {
        'id': 'serial PRIMARY KEY',
        'name': 'varchar(255)',
        'age': 'integer'
    }
    constraints = ['UNIQUE (name)']

    create_table('example_table', columns, constraints)
        """

    # Connect to your PostgreSQL database
    query = f"CREATE TABLE {table_name} ("

    # Add columns to the query
    for column_name, column_type in columns.items():
        query += f"{column_name} {column_type}, "

    # Add constraints to the query
    if constraints:
        query += ", ".join(constraints)

    # Remove the trailing comma and space
    query = query.rstrip(", ") + ")"

    cur.execute(query)


def alter_table(cur, table_name, columns_to_add=None, columns_to_modify=None):
    """
    Alter an SQL table by adding or modifying columns using psycopg2.

    Parameters:
    - table_name (str): The name of the table.
    - columns_to_add (dict, optional): A dictionary where keys are column names and values are column data types.
    - columns_to_modify (dict, optional): A dictionary where keys are column names and values are new column data types.

    Example:
    columns_to_add = {
        'new_column1': 'varchar(255)',
        'new_column2': 'integer'
    }

    columns_to_modify = {
        'existing_column1': 'text',
        'existing_column2': 'date'
    }

    alter_table('example_table', columns_to_add, columns_to_modify)
    """

    # Alter table by adding columns
    if columns_to_add:
        for column_name, column_type in columns_to_add.items():
            cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")

    # Alter table by modifying columns
    if columns_to_modify:
        for column_name, new_column_type in columns_to_modify.items():
            cur.execute(f"ALTER TABLE {table_name} ALTER COLUMN {column_name} TYPE {new_column_type}")


def drop_table(cur, table_name):
    """
    Drop an SQL table using psycopg2.

    Parameters:
    - table_name (str): The name of the table to be dropped.

    Example:
    drop_table('example_table')
    """
    cur.execute(f"DROP TABLE IF EXISTS {table_name}")
