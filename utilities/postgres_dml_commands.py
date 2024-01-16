def insert_actor(cur, first_name, last_name):
    """
        Insert a new actor into the 'actor' table.

        Parameters:
        - cur: psycopg2 cursor object.
        - first_name (str): The first name of the actor.
        - last_name (str): The last name of the actor.

        Returns:
        - int: The actor_id of the newly inserted actor.

        Inserts a new record into the 'actor' table with the provided first name and last name.
        The 'actor_id' of the newly inserted actor is returned.

        Note:
        - It's recommended to use parameterized queries to prevent SQL injection vulnerabilities.
        """
    actor_id = None
    cur.execute(
        f"INSERT into actor(first_name, last_name) values('{first_name}', '{last_name}') returning actor_id;")
    actor_id = cur.fetchone()[0]
    return actor_id


def select_actor(cur, filter_key, value):
    """
        Retrieve actors from the 'actor' table based on a specified filter.

        Parameters:
        - cur: psycopg2 cursor object.
        - filter_key (str): The column to filter on.
        - value: The value to filter by.

        Executes a SELECT query to retrieve actors from the 'actor' table where the specified
        column (filter_key) matches the provided value.
        """
    cur.execute(f"SELECT * FROM actor where {filter_key} = '{value}'")


def select_all_actors(cur):
    """
        Retrieve all actors from the 'actor' table.

        Parameters:
        - cur: psycopg2 cursor object.

        Executes a SELECT query to retrieve all records from the 'actor' table.
        """
    cur.execute("SELECT * FROM actor")


def update_actor_first_name(cur, first_name, actor_id):
    """
        Update the first name of an actor in the 'actor' table.

        Parameters:
        - cur: psycopg2 cursor object.
        - first_name (str): The new first name for the actor.
        - actor_id: The actor_id of the actor to be updated.

        Updates the 'first_name' column of the actor with the specified actor_id in the 'actor' table.
        """
    cur.execute(f"UPDATE actor SET first_name = '{first_name}' WHERE actor_id = {actor_id}")


def delete_actor(cur, actor_id):
    """
        Delete an actor from the 'actor' table.

        Parameters:
        - cur: psycopg2 cursor object.
        - actor_id: The actor_id of the actor to be deleted.

        Deletes the actor with the specified actor_id from the 'actor' table.
        """
    cur.execute(f"DELETE FROM actor WHERE actor_id = {actor_id}")
