import Tyre


class Octoprime(Tyre):
    def __init__(self,TyreWearArray):
        self.TyreWearArray = TyreWearArray
    
    def needs_tobe_serviced(self):
        if sum(self.TyreWearArray) > 3:
            return True
        else:
            return False
