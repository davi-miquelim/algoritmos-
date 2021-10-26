# Creating a graph and finding the shortest path using Djikstra's algorithm

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["end"] = 1
graph["b"]["a"] = 3
graph["b"]["end"] = 5
graph["end"] = {} # The final vertice has no no neighbors

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) # Find the vertice with the lowest cost

while node is not None: # While there are still vertices to process
    cost = costs[node]  
    neighbors = graph[node]
    for n in neighbors.keys(): # For each neighbor of the current node
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # If the new cost is lower than the current cost
            costs[n] = new_cost # Update the cost for the neighbor
            parents[n] = node # Update the parent for the neighbor
    processed.append(node) # Mark the current node as processed
    node = find_lowest_cost_node(costs) # Find the next node to process
