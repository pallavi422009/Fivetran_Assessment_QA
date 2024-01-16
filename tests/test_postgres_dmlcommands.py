from conftest import *
from utilities.postgres_dml_commands import *


@pytest.mark.usefixtures("db_cursor")
class TestPostgresDMLCommand:
    actor_id = None

    def test_add_actor(self):
        """
                Test the addition of an actor to the database.

                Inserts an actor with the name "Jeff Abraham" into the database and
                assigns the generated actor_id to the class variable `actor_id`.
                Checks that the actor_id is not None, prints the actor_id, and commits the changes.

                Raises:
                    Exception: If an error occurs during the execution.
                """
        try:
            TestPostgresDMLCommand.actor_id = insert_actor(self.cur, "Jeff", "Abraham")
            assert TestPostgresDMLCommand.actor_id is not None
            print(TestPostgresDMLCommand.actor_id)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            print(error)
            pytest.fail(error)

    def test_get_actor(self):
        """
                Test the retrieval of actors from the database based on the first name.

                Selects actors with the first name "John" from the database, checks that
                the row count is greater than 0, prints the row count, and displays each retrieved row.

                Raises:
                    Exception: If an error occurs during the execution.
                """
        try:
            select_actor(self.cur, "first_name", "John")
            rows = self.cur.fetchall()
            assert self.cur.rowcount > 0
            print("Number of actors with first_name as John: ", self.cur.rowcount)
            for row in rows:
                print(row)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            pytest.fail(error)

    def test_get_all_actor(self):
        """
                Test the retrieval of all actors from the database.

                Selects all actors from the database, checks that the row count is greater than 0,
                and prints the total number of actors and each retrieved row.

                Raises:
                    Exception: If an error occurs during the execution.
                """
        try:
            select_all_actors(self.cur)
            rows = self.cur.fetchall()
            assert self.cur.rowcount > 0
            print("Total number of actors: ", self.cur.rowcount)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            pytest.fail(error)

    def test_update_actor(self):
        """
                Test the update of an actor's first name in the database.

                Updates the first name of the actor with the stored actor_id to "John",
                checks that the row count is 1, and prints a success message.

                Raises:
                    Exception: If an error occurs during the execution.
                """
        try:
            first_name = "John"
            update_actor_first_name(self.cur, first_name, TestPostgresDMLCommand.actor_id)
            rows = self.cur.rowcount
            assert self.cur.rowcount == 1
            print("Successfully updated first_name")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            pytest.fail(error)

    def test_delete_actor(self):
        """
                Test the deletion of an actor from the database.

                Deletes the actor with the stored actor_id, checks that the row count is 1,
                and prints a success message.

                Raises:
                    Exception: If an error occurs during the execution.
                """
        try:
            delete_actor(self.cur, TestPostgresDMLCommand.actor_id)
            rows = self.cur.rowcount
            assert self.cur.rowcount == 1
            print("Successfully updated first_name")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            pytest.fail(error)
