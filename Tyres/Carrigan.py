import Tyre


class Carrigan(Tyre):
    def __init__(self,TyreWearArray):
        self.TyreWearArray = TyreWearArray
    
    def needs_tobe_serviced(self):
        if any(x >= 0.9 for x in self.TyreWearArray):
            return True
        else:
            return False
