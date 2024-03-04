def and_gate (a, b):

    if a == 1 and b == 1:
      return 1
    else:
      return 0
    
print(and_gate(1,0))


def not_gate (a, b):
    
    if a == 1 and b == 1:
      return 1
    else:
      return 0
    
print(not_gate(1,0))


def or_gate (a, b):

    if a == 1 and b == 1:
      return 1
    else:
      return 1
    
print(or_gate(1,1))
        
        
def xor_gate (a, b):
    
    if a == 1 and b == 1:
      return 1
    else:
      return 0
    
print(xor_gate(1,0))


def nand_gate (a, b):

    if a == 1 and b == 1:
      return 1
    else:
      return 0
    
print(nand_gate(1,0))


def nor_gate (a, b):
    if a == 1 and b == 1:
      return 1
    else:
      return 0
    
print(nor_gate(1,0))


def xnor_gate (a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 1
    
print(xnor_gate(1,1))