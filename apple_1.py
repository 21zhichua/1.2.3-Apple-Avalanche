#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.tracer(False)
  apple.sety(apple.ycor()-40)
  apple.setx(apple.xcor()-18)
  apple.penup()
  apple.color("white")
  apple.write("A", font=("Verdana", 40, "bold"))
  apple.sety(apple.ycor()+40)
  apple.setx(apple.xcor()+18)
  wn.tracer(True)
  wn.update()
def drop_apple():
  apple.penup()
  apple.goto(0,-150)
  apple.pendown()
  apple.clear()
#-----function calls-----
draw_apple(apple)
wn.bgpic("background.gif")
wn.onkeypress(drop_apple,"a")
wn.listen()
wn.mainloop()
