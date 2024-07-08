class dog:
    def __init__(self, name):
        self.name = name
    def barking(self):
        print("bark")
my_dog = dog("bud")
print(my_dog.name)
my_dog.barking()