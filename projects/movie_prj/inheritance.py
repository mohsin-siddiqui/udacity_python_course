class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor gets called!!")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("in class parent")
        print("Last Name = "+self.last_name)
        print("Eye Color = "+self.eye_color)
        print("still in class parent")


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor gets called!!")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("in class child")
        print("Last Name = "+self.last_name)
        print("Eye Color = "+self.eye_color)
        print("Number of toys = "+str(self.number_of_toys))
        print("still in class child")

# billy_cyrus = Parent("Cyrus", "Blue")
# billy_cyrus.show_info()
# print(billy_cyrus.last_name)


miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()
# print(miley_cyrus.last_name)
# print(miley_cyrus.number_of_toys)
