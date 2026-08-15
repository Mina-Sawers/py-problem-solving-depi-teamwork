class MultiplicationTable:
    ''' This class get the multiplication table of a number'''
    def __init__(self,num):
        self._num = num
    def calculate_multiplication_table(self)->None:
        ''' 
        This Function calculate the multiplication table for every number and prints it
        Args:
            num(int): The number from User
        
        '''

        num = self._num

        for i in range (1,11):
            print(f"{num} * {i} = {num*i}")

if __name__ == '__main__':
    mt1 = MultiplicationTable(7)
    mt2 = MultiplicationTable(11)

    mt1.calculate_multiplication_table()
    print("========================")
    mt2.calculate_multiplication_table()
