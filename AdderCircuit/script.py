from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate

def half_adder(a, b):
  c = 0
  s = 0
  if AND_gate(a, b):
    c = 1
  if XOR_gate(a, b):
    s = 1
  return (s, c);

print(half_adder(0, 0))
print(half_adder(0, 1))
print(half_adder(1, 0))
print(half_adder(1, 1))

def full_adder(a, b, c):
  sum1, c1 = half_adder(a, b)
  s, c2 = half_adder(sum1, c)
  c_out = c1 + c2
  return (s, c_out)
print("Full Adder")
print(full_adder(0, 0, 0))
print(full_adder(1, 1, 1))
print(full_adder(0, 1, 1))
print(full_adder(1, 1, 0))

def ALU(a, b, c, opcode):
    if opcode == 0:
      s, c = half_adder(a, b)
    elif opcode == 1:
      s, c = full_adder(a, b, c)
    return (s, c)
print("Testing ALU")
print(ALU(0, 0, 1, 0))
print(ALU(0, 0, 1, 1))
print(ALU(1, 1, 1, 0))
print(ALU(1, 1, 1, 1))