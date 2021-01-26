class electronics:
    no_tv=10
class gadget(electronics):
    no_laptop=20
    no_ac=5
class phone(gadget):
    samsung=10
    nokia=7
    xaiomi=15
    @classmethod
    def change_tv(cls,tv):
        cls.no_tv=tv
    def change_laptop(cls,laptop):
        cls.no_laptop=laptop
    def change_ac(cls,ac):
        cls.no_ac=ac
c1 = electronics()
c2=gadget()
c3=phone()
c3.change_tv(input("Enter No. Of TV = "))
print(c3.no_tv)


