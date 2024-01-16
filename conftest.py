import psycopg2
import pytest

from utilities.config import config


@pytest.fixture(scope="class")
def connect(request):
    """ Connect to the PostgreSQL database server """
    conn = None
    # read connection parameters
    params = config()

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)
    request.cls.conn = conn
    yield conn
    conn.close()
    print("All connections closed successfully")


@pytest.fixture(scope="class")
def db_cursor(request, connect):
    # create a cursor
    cur = connect.cursor()
    request.cls.cur = cur
    yield cur
    cur.close()
    print("Cursor closed successfully")