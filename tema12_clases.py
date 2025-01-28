class OperasBas:
    # #declaracion de propiedades
    # _num1 = 0 #atributo privado public
    # num2 = 0 #atributo publico private
    # __res = 0 #atributo protegido protected
    
    num1 = 0
    num2 = 0
    res = 0
    
    # declaracion de constructor
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    # declaracion de metodos
    def suma(self):
        self.res = self.num1 + self.num2
        print("La suma es: ", self.res)
        return self.res
        
    def resta(self):
        self.res = self.num1 - self.num2
        print("La resta es: ", self.res)
        return self.res

        
def main():
    obj = OperasBas(3, 5)
    obj2 = OperasBas(5, 6)
    
    obj3 = OperasBas(obj.suma(), obj2.resta())
    
    obj3.suma()
    obj3.resta()

    
if __name__ == "__main__":
    main()
