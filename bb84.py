from secret import key_exchange


with open("output") as f:
    lines = f.read().splitlines()
    basis = lines[0][13:-2].split("', '")
    qubits = list(map(complex, lines[1][12:-1].split(", ")))
    myBasis = lines[3][13:-2].split("', '")
    bit_stream = key_exchange(qubits, basis, myBasis)
    out = int(lines[5])
    print(hex(int(bit_stream[:400],2) ^ out))