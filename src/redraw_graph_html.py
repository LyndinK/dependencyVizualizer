from src.network_wrapper import NetworkWrapper
from src.config import COLOURS


def determine_colour(status: str) -> str:
    if status == 'ERROR':
        return 'red'
    elif status == 'SUCCESS':
        return 'green'
    elif status == 'PENDING':
        return 'gray'
    elif status == 'RUNNING':
        return 'blue'
    else:
        return 'white'


def redraw_graph_html(nodes: list, edges: list) -> None:
    ntw = NetworkWrapper('100vh', '100vw', directed=True)
    # nodes
    for node in nodes:
        ntw.add_node(node[0],
                     label=node[1],
                     color=COLOURS[determine_colour(node[2])],
                     shape='box',
                     title=f"""
                             start: {str(node[3])} \n
                             end: {str(node[4])} \n
                             duration: {node[5]}
                            """
                     )
    # edges
    if edges:
        for edge in edges:
            ntw.add_edge(*edge)
    ntw.write_html()
