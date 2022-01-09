class Bush:
    def __init__(self):
        self.type = "";
        self.name = "";
        

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.type = str(strArray[i])
        self.name = str(strArray[i+1])
        i += 2
        #print("Bush: type = ", self.type, " name = ", self.name)
        return i

    def Print(self):
        print("Bush: type = ", self.type, " name = ", self.name, ", Quotient = ", self.Quotient())
        pass

    def Write(self, ostream):
        ostream.write("Bush: type = {}  name = {}, Quotient = {}".format(self.type, self.name, self.Quotient()))
        pass

    def Quotient(self):
        vowel[12] = "AEIOUYaeiouy";
        sum_char = 0
        sum_vowel = 0
        for i in range(10):
            sum_char+=1
            for j in range(12):
                if (self.name[i] == vowel[j]):
                    sum_vowel+=1 
        return double(sum_vowel / sum_char);
        pass