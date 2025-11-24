from ..base import Operation
class mean(Operation):
        def __init__(self,*args):
            self.obj = args

        def execute(self):
            return sum(self.obj)/len(self.obj)
