import os

# -----------------
# general
# -----------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
TEMPLATES = os.path.join(PROJECT_ROOT, 'templates')

# -----------------
# visualization
# -----------------
GRAPH_VIZ_OPTIONS = {'nodes':  # options for graph visualizer
                         {'shape': 'dot',
                          'size': 10},
                     'edges':
                         {'color': {'inherit': True},
                          'smooth': False},
                     'layout':
                         {'hierarchical':
                              {'enabled': True, 'direction': 'LR', 'sortMethod': 'directed'}},
                     'interaction':
                         {'navigationButtons': True},
                     'physics':
                         {'hierarchicalRepulsion':
                              {'centralGravity': 0,
                               'springLength': 75,
                               'nodeDistance': 200,
                               'damping': 0.2},
                          'maxVelocity': 28,
                          'minVelocity': 0.75,
                          'solver': 'hierarchicalRepulsion'}}

COLOURS = {  # set colours for graph elements
    'green': '#c1f07f',
    'red': "#e87474",
    'gray': '#b3b3b3',
    'dark gray': '#424242',
    'white': '#ffffff',
    'blue': '#36d1c4'
}

# -----------------
# database
# -----------------
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5433')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
