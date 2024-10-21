import random
from pyvis.network import Network
import json

# Function to create random sets of people and topics
def generate_random_people_and_topics(num_people=5, num_topics=5):
    people = [f'Person {i}' for i in range(1, num_people + 1)]
    topics = [f'Idea {i}' for i in range(1, num_topics + 1)]
    return people, topics

# Function to generate random edges with a limit of up to 3 edges per person
def generate_random_edges(people, topics, max_edges_per_person=3):
    edges = []
    for person in people:
        # Ensure that the number of edges for this person is between 1 and max_edges_per_person
        num_edges = random.randint(1, min(max_edges_per_person, len(topics)))  # max of 3 edges or less if topics are fewer
        chosen_topics = random.sample(topics, num_edges)  # Randomly choose topics
        edges.extend([(person, topic) for topic in chosen_topics])
    return edges

# Function to create the JSON structure from nodes and edges
def create_json_structure(people, topics, edges):
    # Prepare nodes
    nodes = []
    for topic in topics:
        nodes.append({
            "id": topic,
            "height": 50,
            "fill": {"src": "idea.webp"}  # Assuming all topics have the same image
        })
    for person in people:
        nodes.append({
            "id": person,
            "height": 50,
            "fill": {"src": "person.webp"}  # Assuming all people have the same image
        })
    
    # Prepare edges
    edges_list = [{"from": person, "to": topic} for person, topic in edges]
    
    return {"nodes": nodes, "edges": edges_list}

# Function to create and visualize the graph
def create_visualization(other_nodes, idea_nodes, edges, output_file='network.html', json_file='network.json'):
    net = Network(notebook=False)
    
    # Add people and ideas to the network
    for node in idea_nodes:
        net.add_node(node, label=node, color='skyblue', title=node)

    for node in other_nodes:
        net.add_node(node, label=node, color='lightcoral', title=node)
    
    # Add edges between people and ideas
    for edge in edges:
        net.add_edge(edge[0], edge[1], smooth=False, color='gray')
    
    for node in net.get_nodes():
        net.get_node(node)['physics']=False
    
    # Set options
    net.toggle_physics(False)

    # Generate and save the HTML file
    net.show(output_file, notebook=False)
    print(f"Network visualization saved as {output_file}")

    # Create JSON structure and save to a file
    json_structure = create_json_structure(people, topics, edges)
    with open(json_file, 'w') as f:
        json.dump(json_structure, f, indent=2)
    print(f"JSON data saved as {json_file}")



for i in range(0,40):
    num_people=random.randint(5, 30)
    num_topics=random.randint(5, 30)
    output_file=f'Ilaria-code/random/graph{i}.html'
    json_file=f'Ilaria-code/random/json/data_images{i}.json'
    people, topics = generate_random_people_and_topics(num_people, num_topics)
    edges = generate_random_edges(people, topics)
    create_visualization(people, topics, edges, output_file,json_file)

