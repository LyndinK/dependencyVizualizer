from pyvis.network import Network
from jinja2 import Template
from src.config import GRAPH_VIZ_OPTIONS, TEMPLATES
import os


class NetworkWrapper(Network):
    """Inherits the original class in order to correct a few things"""

    def __init__(self, height="500px", width="500px", directed=True, notebook=False, bgcolor="#ffffff",
                 font_color=False, layout=None, heading="", options_=GRAPH_VIZ_OPTIONS, ):
        super().__init__(height, width, directed, notebook, bgcolor, font_color, layout, heading)
        self.options = options_

    def write_html(self, notebook=False):
        """
        This method gets the data structures supporting the nodes, edges,
        and options and updates the template to generate the HTML holding
        the visualization.

        OVERLOADED: The original class had no method to generate the html without writing it out on disk
        """
        # here, check if an href is present in the hover data
        use_link_template = False
        for n in self.nodes:
            title = n.get("title", None)
            if title:
                if "href" in title:
                    """
                    this tells the template to override default hover
                    mechanic, as the tooltip would move with the mouse
                    cursor which made interacting with hover data useless.
                    """
                    use_link_template = True
                    break
        if not notebook:
            with open(self.path) as html:
                content = html.read()
            template = Template(content)
        else:
            template = self.template

        nodes, edges, heading, height, width, options = self.get_network_data()

        # check if physics is enabled
        if isinstance(self.options, dict):
            if 'physics' in self.options and 'enabled' in self.options['physics']:
                physics_enabled = self.options['physics']['enabled']
            else:
                physics_enabled = True
        else:
            physics_enabled = self.options.physics.enabled

        self.html = template.render(height=height,
                                    width=width,
                                    nodes=nodes,
                                    edges=edges,
                                    heading=heading,
                                    options=options,
                                    physics_enabled=physics_enabled,
                                    use_DOT=self.use_DOT,
                                    dot_lang=self.dot_lang,
                                    widget=self.widget,
                                    bgcolor=self.bgcolor,
                                    conf=self.conf,
                                    tooltip_link=use_link_template)

        # replace global library with the local scripts
        self.html = self.html.replace('https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis.css',
                                      """{{url_for('static', filename='vis.css')}}""")
        self.html = self.html.replace('https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis-network.min.js',
                                      """{{url_for('static', filename='vis.js')}}""")

        with open(os.path.join(TEMPLATES, 'nx.html'), 'w') as f:
            f.write(self.html)
