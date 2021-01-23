from animalandcat.animal import Animal

class Cat(Animal):

    def __init__(self,name,colour,age,gender):
        self.hair = "短毛"
        super().__init__(name,colour,age,gender)

    def catching_mice(self):
        print("会捉老鼠")

    def call(self):
        print("喵喵叫")

if __name__ == '__main__':
    cat01 = Cat("cat1","white",2,"male")
    cat01.catching_mice()
    cat01.call()
    cat01.run()
    print(cat01.hair)

