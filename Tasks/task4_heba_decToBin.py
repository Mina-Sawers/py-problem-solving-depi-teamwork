'''
this function converts a decimal number to binary number
Args:
    Num (int): number input from the user
Returns:
    bnum (binary): the binary representation of the number
'''

def decToBin(num: int):
    return bin(int(num))[2:]



if __name__ == "__main__":
    x= input("enter a decimal number to convert to binary number:")
    print (decToBin(x))
