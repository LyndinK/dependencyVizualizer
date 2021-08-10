import psycopg2
from psycopg2 import OperationalError
from src.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


def query_database() -> (list, list):
    # a query to select the nodes
    query_nodes = """
                        select object_id
                              ,object_name
                              ,status
                              ,start_dttm
                              ,finish_dttm
                              ,duration
                        from test_etl.object_loader_log
                   """

    # a query to select the edges
    query_edges = """
                        select parent_node_id
                              ,child_node_id
                        from test_etl.object_load_dependency
                  """
    try:
        with psycopg2.connect(host=DB_HOST,
                              port=DB_PORT,
                              dbname=DB_NAME,
                              user=DB_USER,
                              password=DB_PASSWORD) as conn:
            cursor = conn.cursor()
            # get nodes
            cursor.execute(query_nodes)
            nodes = cursor.fetchall()
            # get edges
            cursor.execute(query_edges)
            edges = cursor.fetchall()
    except OperationalError:
        nodes = [(1, 'CANT_CONNECT_TO_DATABASE', 'ERROR', '', '', '')]
        edges = []
    finally:
        return nodes, edges
