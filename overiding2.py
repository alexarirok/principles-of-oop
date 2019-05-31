class A:
    def explore(self):
        print("explore() method class A")

class B(A):
    def explore(self):
        super().explore() #accessing the overridden method of the parent class in the child class, you can call it using the super()
        print("explore() method from class B")

b_obj = B()
b_obj.explore()