from ir_generator import generate_ir
from liveness import liveness_analysis
from reg_alloc import build_interference_graph, allocate_registers

with open("sample_input.txt") as f:
    lines = f.readlines()

ir = generate_ir(lines)
live_ranges = liveness_analysis(ir)
graph = build_interference_graph(live_ranges)
register_assignment = allocate_registers(graph)

print("IR:", ir)
print("Live Ranges:", live_ranges)
print("Register Mapping:", register_assignment)
