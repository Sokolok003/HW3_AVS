import bush
import tree
import flower

#----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    #def ReadStrArray(self, strArray):

    def Print(self):
        print("Container is store", len(self.store), "plants:")
        for plant in self.store:
            plant.Print()
        print("Summa of Quotients  = ", self.Quotient())
        pass

    def Write(self, ostream):
        ostream.write("Container is store {} plants:\n".format(len(self.store)))
        for plant in self.store:
            plant.Write(ostream)
            ostream.write("\n")
        ostream.write("Summa of Quotient  = {}\n".format(self.Quotient()))
        pass

    def Quotient(self):
        sum = 0.0
        for plant in self.store:
            sum += plant.Quotient()
        return sum

    def OnlyTreeQuotient(self):
        sum = 0.0
        for plant in self.store:
            #print(type(plant))
            if isinstance(plant, tree.Tree):
                sum += plant.Quotient()
        return sum

    def OnlyBushQuotient(self):
        sum = 0.0
        for plant in self.store:
            #print(type(plant))
            if isinstance(plant, bush.Bush):
                sum += plant.Quotient()
        return sum

    def OnlyFlowerQuotient(self):
        sum = 0.0
        for plant in self.store:
            #print(type(plant))
            if isinstance(plant, flower.Flower):
                sum += plant.Quotient()
        return sum
