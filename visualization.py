from pyvis.network import Network
from value import Value

import uuid

def visualize_computational_graph(last_node: Value, file_path: str, verbose=False):
  # Used to track visited nodes during DFS
  visited = set()

  # Create and configurate the visualization tool
  net = Network(directed=True)
  net.set_options("""
    {
      "layout": {
        "hierarchical": {
          "enabled": true,
          "direction": "UD",
          "sortMethod": "directed"
        }
      },
      "nodes": {
        "font": {
          "size": 18,
          "face": "courier",
          "color": "#333"
        }
      },
      "physics": {
        "enabled": true,
        "hierarchicalRepulsion": {
          "nodeDistance": 180,
          "centralGravity": 0.0,
          "springLength": 100,
          "springConstant": 0.01,
          "damping": 0.09
        },
        "stabilization": {
          "iterations": 250
        }
      }
    }
  """)

  # Track all nodes and edges in the graph
  _visualize_computational_graph(last_node, visited, net, verbose)

  display_in_html_file(net, file_path)

def _visualize_computational_graph(node: Value, visited: set[str], graph, verbose: bool):
  if node in visited:
    return

  visited.add(node)

  verbose_info = f'{node.label}\n——\nd: {node.data:.2f}\ng: {node.gradient:.2f}'

  if verbose:
    info = verbose_info
    styles = {"color": "white", "align": "left"}
  else:
    info = f'{node.label}'
    styles = {"color": "white"}

  if node._operator:
    graph.add_node(
      id(node),
      label=f'{info}\n——\n{node._operator}',
      label_properties={
        "align": "left"
      },
      title=f'{verbose_info}\n——\n{node._operator}',
      color={
        "background": "#000000",
        "border": "#ffffff"
      },
      shape="box",
      font= styles
    )
  else:
    graph.add_node(
      id(node),
      label=info,
      label_properties={
        "align": "left"
      },
      title=verbose_info,
      color={
        "background": "#343434",
        "border": "#ffffff"
      },
      shape="box",
      font=styles
    )

  for parent in node.parents:
    _visualize_computational_graph(parent, visited, graph, verbose)

    graph.add_edge(id(parent), id(node), color="white")

def display_in_html_file(net: Network, file_path: str):
  # Display the graph
  html = net.generate_html()

  # Patch vertical centering and add extra styles
  html = html.replace(
    """
             #mynetwork {
                 width: 100%;
                 height: 600px;
                 background-color: #ffffff;
                 border: 1px solid lightgray;
                 position: relative;
                 float: left;
             }
""",
    """
             #mynetwork {
                 width: 100%;
                 height: 100vh;
                 background-color: #000000;
                 border: 1px solid lightgray;
                 position: relative;
                 float: left;
             }

            html, body {
              height: 100%;
              margin: 0;
            }

            body {
              display: flex;
              align-items: center;      /* vertical centering */
              justify-content: center;  /* horizontal centering */
            }
"""
)

  with open(file_path, "w") as f:
      f.write(html)

def generate_id() -> str:
  return str(uuid.uuid4())

