class Pole:
    NoPrivatPoleA="1"
    __PrivatPoleB="2"
    __PrivatPoleC="3"

    #PoleA 
    def get_NoPrivatPoleA():
        return PrivatPoleA

    def set_NoPrivatPoleA(self, func1):
        self.NoPrivatPoleA=func1

    #PoleB  
    def get_PrivatPoleB():
        return PrivatPoleB

    def set_PrivatPoleB(self, func2):
        self.PrivatPoleB=func2

    #PoleC 
    def get_PrivatPoleC():
        return PrivatPoleC

    def set_PrivatPoleC(self, func3):
        self.PrivatPoleC=func3
Pole2=Pole()
print(Pole2.NoPrivatPoleA)
Pole2.NoPrivatPoleA="1+x"
print(Pole2.NoPrivatPoleA)
print()