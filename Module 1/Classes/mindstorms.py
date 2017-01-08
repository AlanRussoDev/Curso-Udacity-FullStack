import turtle

def draw_square():
           
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)
      
    for i in range(0,4):
        brad.forward(100)
        brad.right(90)
        
 


def draw_circle():
    
    window = turtle.Screen()
    window.bgcolor("red")  
           
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)
    
    window.exitonclick()

    

def draw_example():

    window = turtle.Screen()
    window.bgcolor("blue")  
           
    circle = turtle.Turtle()
    circle.speed(10)

    for i in range(180):
        circle.forward(100)
        circle.right(30)
        circle.forward(20)
        circle.left(60)
        circle.forward(50)
        circle.right(30)
        
        circle.penup()
        circle.setposition(0, 0)
        circle.pendown()
        
        circle.right(2)

draw_example()
        
