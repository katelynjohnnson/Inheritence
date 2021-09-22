
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color


class Flower(Plant):
    def __init__(self,color, petals):
        Plant.__init__(self,color)

        self.__petals = petals

    def get_petals(self):
        return self.__petals
    
