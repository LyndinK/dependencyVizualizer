from flask import Flask, render_template
from src.redraw_graph_html import redraw_graph_html
from src.query_database import query_database


app = Flask(__name__)


@app.route('/')
def redraw_node_graph():
    nodes, edges = query_database()
    redraw_graph_html(nodes, edges)
    return render_template("nx.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
