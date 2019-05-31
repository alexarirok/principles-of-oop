"""class Jester:
    def laugh(self):
        return print("laugh() called")

obj = Jester
print(obj)"""

#overriding this method by defining a method named __str__() in the Jester class

class Jester:
    def laugh(self):
        return "laugh() called"

    def __str__(self):
        return "A more helpful description"

obj = Jester()
print(obj)