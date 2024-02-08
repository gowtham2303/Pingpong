from turtle import Turtle



class Ball (Turtle):

    def __init__(self) :
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.x_movement =10
        self.y_movement =10
        self.move_speed = 0.1

    def move (self):
        x_pos=self.xcor()+ self.x_movement
        y_pos=self.ycor()+ self.y_movement
        self.goto(x_pos,y_pos)
        
    def y_bounce (self):
       self.y_movement *=-1
    #    self.move_speed = 0.9

    def x_bounce (self):
        self.x_movement *=-1
        self.move_speed  *= 0.9

    def reset_positoin (self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.x_bounce()
