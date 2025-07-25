def generate_ir(lines):
    # 假設每行都已是最簡單的三地址格式
    ir = []
    for line in lines:
        ir.append(line.strip())
    return ir
