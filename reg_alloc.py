def build_interference_graph(live_ranges):
    variables = list(live_ranges.keys())
    graph = {var: set() for var in variables}
    for i in range(len(variables)):
        for j in range(i+1, len(variables)):
            a, b = variables[i], variables[j]
            ra, rb = live_ranges[a], live_ranges[b]
            if not (ra[1] < rb[0] or rb[1] < ra[0]):
                graph[a].add(b)
                graph[b].add(a)
    return graph

def allocate_registers(graph, num_registers=3):
    registers = ['R'+str(i+1) for i in range(num_registers)]
    assignment = {}
    for var in graph:
        used = {assignment[adj] for adj in graph[var] if adj in assignment}
        for reg in registers:
            if reg not in used:
                assignment[var] = reg
                break
        else:
            assignment[var] = "SPILL"
    return assignment
