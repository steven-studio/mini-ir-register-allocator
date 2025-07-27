def parse_ir(lines):
    # 假設每行已經是簡單三地址碼，例如：a = b + c
    ir = []
    for line in lines:
        ir.append(line.strip())
    return ir

def compute_live_intervals(ir):
    # key: 變數, value: [start, end]
    intervals = {}
    for idx, line in enumerate(ir):
        tokens = line.replace('=', ' ').replace('+', ' ').replace('*', ' ').replace('return', ' ').split()
        for t in tokens:
            if t.isalpha():
                if t not in intervals:
                    intervals[t] = [idx, idx]
                else:
                    intervals[t][1] = idx
    return intervals

def linear_scan_allocate(intervals, num_registers=3):
    # intervals: dict 變數->[start, end]
    intervals_list = sorted([(v, start, end) for v, (start, end) in intervals.items()], key=lambda x: x[1])
    active = []
    registers = ['R' + str(i+1) for i in range(num_registers)]
    assignment = {}

    def expire_old_intervals(var_start):
        nonlocal active
        active = [item for item in active if item[2] >= var_start]

    for var, start, end in intervals_list:
        expire_old_intervals(start)
        if len(active) == num_registers:
            # Spill策略：這裡簡化為spill最晚結束的
            spill = max(active, key=lambda x: x[2])
            assignment[var] = 'SPILL'
        else:
            # 分配尚未被占用的register
            used_regs = {assignment[item[0]] for item in active}
            for reg in registers:
                if reg not in used_regs:
                    assignment[var] = reg
                    break
            active.append((var, start, end))
    return assignment

# --- 範例流程 ---
if __name__ == "__main__":
    lines = [
        "a = 1",
        "b = 2",
        "c = a + b",
        "d = c * 5",
        "return d"
    ]
    ir = parse_ir(lines)
    intervals = compute_live_intervals(ir)
    reg_map = linear_scan_allocate(intervals, num_registers=3)
    print("Live Intervals:", intervals)
    print("Register Assignment:", reg_map)
