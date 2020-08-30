class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):

    div_sum = 0
    
    def divisorSum(self, n):
        for number in range(1, int((n/2)+1)):
            if (n % number == 0):
                self.div_sum += number
        
        return self.div_sum+n


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)