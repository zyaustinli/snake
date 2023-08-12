from turtle import Turtle




STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

UP= 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        
        self.segments=  []
        self.create_snake()

        self.head=self.segments[0]


    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def move(self):
        
        for seg_num in range(len(self.segments)-1,0,-1): #starts from end of tail
            new_x = self.segments[seg_num-1].xcor()        #coords of previous segment
            new_y = self.segments[seg_num-1].ycor()        
            self.segments[seg_num].goto(new_x,new_y)  #move last segment of tail to one tile in front
        self.head.forward(MOVE_DISTANCE) #after 3 has moved to 2 and 2 has moved to 1, 1 needs to move forward

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

        
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
      
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
      
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
       