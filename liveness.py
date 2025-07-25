def liveness_analysis(ir):
    uses = {}
    for idx, line in enumerate(ir):
        tokens = line.replace('=', ' ').replace('+', ' ').replace('*', ' ').replace('return', ' ').split()
        for t in tokens:
            if t.isalpha():
                if t not in uses:
                    uses[t] = [idx, idx]
                else:
                    uses[t][1] = idx
    return uses
