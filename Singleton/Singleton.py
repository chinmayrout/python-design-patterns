"""
This pattern restricts the instantiation of a class to one object. 
It is a type of creational pattern and involves only one class to create methods and specified objects.

It provides a global point of access to the instance created.

"""

class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """Static access method."""
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """Virtually private constructor."""
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)
