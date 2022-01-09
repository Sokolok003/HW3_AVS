from extender import *

def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0   # Индекс, задающий текущую строку в массиве
    figNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)   # преобразование в целое 
        #print("key = ", key)
        if key == 1: # признак куста
            i += 1
            plant = Bush()
            i = plant.ReadStrArray(strArray, i) # чтение куста с возвратом позиции за ним
        elif key == 2: # признак цветка
            i += 1
            plant = Flower()
            i = plant.ReadStrArray(strArray, i) # чтение цветка с возвратом позиции за ним
        elif key == 3: # признак дерева
           i += 1
           plant = Tree()
           i = plant.ReadStrArray(strArray, i) # чтение дерева с возвратом позиции за ним           
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных растений
            return figNum
        # Количество пробелами растений увеличивается на 1
        if i == 0:
            return figNum
        figNum += 1
        container.store.append(plant)
    return figNum
