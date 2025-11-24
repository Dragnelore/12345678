from ..base import Operation

class factorial(Operation):
    def __init__(self,a):
        self.a = a 

    def factorial(self,a):
        if a <= 1:
            return 1
        else:
            return self.factorial(a-1) * a

    def execute(self):
        return self.factorial(self.a)
