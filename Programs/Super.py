class A:
    classvar1="I am in Class A Cariable\n"
    def __init__(self):
        self.classvar1 = "I am In Class A Instance Variable\n"
        self.var1="I am In Instance Variable\n"
class B(A):
    classvar1 = "I Ma In Class B\n"
    def __init__(self):
        self.classvar1 = "I am In Class B Instance Variable\n"
        self.var1 = "I am In Instance Variable in B\n"
        super().__init__()


v1=B()
print(v1.classvar1)#Due to super at last i can access class A variables
#But if super was at first than first it acess class A variable and than changes to B
print(v1.var1)

