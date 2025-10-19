from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hlo(self):
        pass


class English(Greet):
    def say_hlo(self):
        return "Hello!"
    
class Hindi(Greet):
    def say_hlo(self):
        return "Ram Ram"
    
g = Hindi()
print(g.say_hlo())