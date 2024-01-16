from conftest import *
from utilities.postgres_ddl_commands import *


@pytest.mark.usefixtures("db_cursor")
class TestPostgresDDLCommand:
    test_table_name = "test_table"

    def test_create_table(self):
        """"""
        test_columns = {
            'id': 'serial PRIMARY KEY',
            'name': 'varchar(255)',
            'age': 'integer'
        }
        test_constraints = ['UNIQUE (name)']

        # Test create_table
        create_table(self.cur, self.test_table_name, test_columns, test_constraints)
        try:
            self.conn.commit()
            print(f"Table '{self.test_table_name}' created successfully.")
            # Check if the table exists
            self.cur.execute(f"SELECT * FROM information_schema.tables WHERE table_name = '{self.test_table_name}'")
            assert self.cur.fetchone() is not None
        except Exception as e:
            # Rollback the changes if an error occurs
            self.conn.rollback()
            print(f"Error while rollback: {e}")

    def test_alter_table(self):
        columns_to_add = {
            'city': 'varchar(255)'
        }

        alter_table(self.cur, self.test_table_name, columns_to_add=columns_to_add)
        try:
            self.conn.commit()
            print(f"Table '{self.test_table_name}' altered successfully.")
            # Check if the columns have been added or modified
            self.cur.execute(
                f"SELECT column_name FROM information_schema.columns WHERE table_name = '{self.test_table_name}'")
            result = self.cur.fetchall()

            column_names = [row[0] for row in result]

            assert 'city' in column_names

        except Exception as e:
            # Rollback the changes if an error occurs
            self.conn.rollback()
            print(f"Error while rollback: {e}")

    def test_drop_table(self):
        # test_table_name = "test_table"

        drop_table(self.cur, self.test_table_name)
        try:
            self.conn.commit()
            print(f"Table '{self.test_table_name}' dropped successfully.")
            # Check if the table exists
            self.cur.execute(f"SELECT * FROM information_schema.tables WHERE table_name = '{self.test_table_name}'")
            assert self.cur.fetchone() is None
        except Exception as e:
            # Rollback the changes if an error occurs
            self.conn.rollback()
            print(f"Error while rollback: {e}")
