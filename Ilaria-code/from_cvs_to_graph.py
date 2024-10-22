import csv
import networkx as nx
from pyvis.network import Network


# Path to your CSV file
file_path = 'ideas_map_data.csv'

# Initialize an empty dictionary
csv_dict = {}

# Open the file and read its contents
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Loop through the rows and update the dictionary
    for row in csv_reader:
        for key, value in row.items():
            if key in csv_dict:
                csv_dict[key].append(value)
            else:
                csv_dict[key] = [value]



names = []
positions = []
topics = []
descriptions = []

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        names.append(row['Name']+ ' '+row['Surname'])
        positions.append(row['Position'])
        topics.append(row['Your topic (maximum 2 words)'])
        descriptions.append(row['A brief explanation of your topic'])

# G = nx.Graph()

# for i in range(len(names)):
#     name_node = names[i]
#     topic_node = topics[i]
    
#     # Add name node with position as an attribute
#     G.add_node(name_node, type='name', position=positions[i])
    
#     # Add topic node with description as an attribute
#     G.add_node(topic_node, type='topic', description=descriptions[i])
    
#     # Create an edge between the name and topic
#     G.add_edge(name_node, topic_node)


net = Network(notebook=False)
added_nodes = set()

# Step 3: Add nodes and edges to the graph
for i in range(len(names)):
    name_node = names[i]
    topic_node = topics[i]
    
    # Add name node if not already added
    if name_node not in added_nodes:
        net.add_node(name_node, label=name_node, title=positions[i], color='lightcoral')
        added_nodes.add(name_node)
    
    # Add topic node if not already added
    if topic_node not in added_nodes:
        net.add_node(topic_node, label=topic_node, title=descriptions[i], color='skyblue')
        added_nodes.add(topic_node)
    
    # Create an edge between the name and topic
    net.add_edge(name_node, topic_node)

# Step 4: Show the network in a browser
net.show('first_data.html', notebook=False)