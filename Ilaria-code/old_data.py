from pyvis.network import Network
import json

with open('data_images.json', 'r') as f:
    data = json.load(f)

# Separate nodes based on 'fill.src' value
idea_nodes = [node['id'] for node in data['nodes'] if (node['fill']['src'] == 'idea.webp' or node['fill']['src'] == 'https://awoiaf.westeros.org/images/thumb/d/d5/House_Lannister.svg/500px-House_Lannister.svg.png')]
other_nodes = [node['id'] for node in data['nodes'] if (node['fill']['src'] != 'idea.webp' and node['fill']['src'] != 'https://awoiaf.westeros.org/images/thumb/d/d5/House_Lannister.svg/500px-House_Lannister.svg.png')]

# Extract edges
edges = [(edge['from'], edge['to']) for edge in data['edges'] if edge['from'] and edge['to']]

# Create a pyvis network
net = Network(notebook=False)

# Add nodes with different colors for idea_nodes and other_nodes
for node in idea_nodes:
    net.add_node(node, label=node, color='skyblue', title=node)

for node in other_nodes:
    net.add_node(node, label=node, color='lightcoral', title=node)

# Add edges
for edge in edges:
    net.add_edge(edge[0], edge[1], smooth=False, color='gray')

for node in net.get_nodes():
  net.get_node(node)['physics']=False
 
  


net.toggle_physics(False)

# Generate and save the HTML file
net.show('people_2.html', notebook=False)