class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent COntructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name - " + self.last_name)
        print("Eye color - " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Contructor Called")
        Parent.__init__(self, last_name, eye_color)       
        self.number_of_toys = number_of_toys
     

 
#billy_cyrus = Parent("Cyrus","blue")
#print(billy_cyrus.eye_color)

milley_cyrus = Child("Cyrus","blue",5)
milley_cyrus.show_info()
#print(milley_cyrus.number_of_toys)
