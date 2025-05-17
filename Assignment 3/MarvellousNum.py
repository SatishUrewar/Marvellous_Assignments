def ChkPrime(B):
    if B < 2:
        return False
    for i in range(2,B):
     if (B % i==0):
        return  False
     
    return True

def sum(X,Y):
     return X+Y 