def calculate_multiplication_table(num:int)->None:
    ''' 
    This Function calculate the multiplication table for every number and prints it
    Args:
        num(int): The number from User
    
    '''
    for i in range (1,11):
        print(f"{num} * {i} = {num*i}")

if __name__ == '__main__':
    calculate_multiplication_table(6)
