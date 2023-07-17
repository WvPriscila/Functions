
def P_Normal(a):
    
    # Porta Normal  
    if a == 0:
        return 0
    if a == 1:
        return 1


def P_inversora(a):
    
    # Porta contrária
    if a == 0:
        return 1
    if a ==1:
        return 0

def P_AND(a,b):
    if a == b:
        if a == 0:
            return 0
        if a == 1:
            return 1
    if a != b:
        return 0

def P_NAND(a,b):
    if a == b:
        if a == 0:
            return 1
        if a == 1:
            return 0
    if a != b:
        return 1
        
def P_OR(a,b):
    if a == b:
        if a == 0:
            return 0
        if a == 1:
            return 1
    if a != b:
        return 1
        
def P_NOR(a,b):
    if a == b:
        if a == 0:
            return 1
        if a == 1:
            return 0
    if a != b:
        return 0
        
def XOR(a,b):
    if a == b:
        if a == 0:
            return 0
        if a == 1:
            return 0
    if a != b:
        return 

def XNOR(a,b):
    if a == b:
        if a == 0:
            return 1
        if a == 1:
            return 1
    if a != b:
        return 0
    
    
    
