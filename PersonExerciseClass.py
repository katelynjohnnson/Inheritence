class Person:
    def __init__(self,name,address,telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone

    def print_person(self):
        return (self.__name, self.__address, self.__telephone)


    class Customer(Person):
        def __init__(self,name,address,telephone,custnum,onlist):
            Person.__init__(self,name,address,telephone)

            self.__custnum = custnum
            self.__onlist = onlist

        def get_custnum(self):
            return self.__custnum


###THIS IS NOT DONE! REEVALUATE!!!!###