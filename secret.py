# FLAG="AIS3{FLAGGGGG}"
a = 0x414953337b71717171
b = 0x727272727272727272
p = 0x737373737373737373
FLAG=0x414953337b71717171727272727272727272737373737373737373


dic = {(1+0j): "↑",
       (0+1j): "→",
       (0.707+0.707j): "↗",
       (0.707-0.707j): "↘"}

arrow = {"↑": '0', "→": '1', "↗": '0', "↘": '1'}

def key_exchange(qubits, basis, myBasis):
    for i, q in enumerate(qubits):
        qubits[i] = dic[q]
    res = ""
    for q, a, b in zip(qubits, basis, myBasis):
        if a != b:
            continue
        res += arrow[q]
    return res





